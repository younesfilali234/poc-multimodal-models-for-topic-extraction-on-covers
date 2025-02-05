import logging
import json
import traceback
from typing import List, Dict, Any
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)


class DatabaseHandler:
    def __init__(self, db_path: str) -> None:
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.Session = sessionmaker(bind=self.engine)
        self.metadata = MetaData()

    def save_data(self, table_name: str, data: Dict[str, Any]) -> None:
        with self.Session() as session:
            try:
                table = Table(table_name, self.metadata, autoload_with=self.engine)
                session.execute(
                    table.insert().values(
                        {
                            key: json.dumps(value)
                            if isinstance(value, (list, dict))
                            else value
                            for key, value in data.items()
                        }
                    )
                )
                session.commit()
                logger.info(f"Data saved to table '{table_name}': {data}")
            except SQLAlchemyError as e:
                logger.error(
                    f"Database save failed for table '{table_name}': {e}\n{traceback.format_exc()}"
                )
                session.rollback()

    def fetch_data(self, table_name: str) -> List[Dict[str, Any]]:
        with self.Session() as session:
            try:
                table = Table(table_name, self.metadata, autoload_with=self.engine)
                result = session.execute(table.select()).all()
                data = [dict(row._mapping) for row in result]
                logger.info(f"Fetched {len(data)} rows from table '{table_name}'.")
                return data
            except SQLAlchemyError as e:
                logger.error(
                    f"Error fetching data from table '{table_name}': {e}\n{traceback.format_exc()}"
                )
                return []
