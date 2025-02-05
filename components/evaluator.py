import os
import csv
import json
import logging
from fuzzywuzzy import fuzz
from components.database_handler import DatabaseHandler
from settings import GROUND_TRUTH_DB_PATH, PREDICTIONS_DB_PATH, EVALUATION_RESULTS_PATH

logger = logging.getLogger(__name__)


def evaluate_predictions():
    """Compares predictions with ground truth data and saves the results."""
    logger.info("Starting evaluation...")

    ground_truth_handler = DatabaseHandler(db_path=GROUND_TRUTH_DB_PATH)
    predictions_handler = DatabaseHandler(db_path=PREDICTIONS_DB_PATH)

    ground_truth = ground_truth_handler.fetch_data("ground_truth")
    predictions = predictions_handler.fetch_data("predictions")

    os.makedirs(os.path.dirname(EVALUATION_RESULTS_PATH), exist_ok=True)

    with open(
        EVALUATION_RESULTS_PATH, mode="w", newline="", encoding="utf-8"
    ) as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "ID",
                "Headline (Ground Truth)",
                "Protagonists (Ground Truth)",
                "Headline (Prediction)",
                "Protagonists (Prediction)",
                "Headline Similarity (%)",
                "Protagonists Similarity (%)",
            ],
        )
        writer.writeheader()

        for truth in ground_truth:
            prediction = next(p for p in predictions if p["id"] == truth["id"])

            truth_protagonists = json.loads(truth.get("protagonists"))
            prediction_protagonists = json.loads(prediction.get("protagonists"))

            headline_similarity = fuzz.ratio(
                truth.get("headline"), prediction.get("headline")
            )
            protagonists_similarity = fuzz.ratio(
                ", ".join(truth_protagonists), ", ".join(prediction_protagonists)
            )

            writer.writerow(
                {
                    "ID": truth["id"],
                    "Headline (Ground Truth)": truth["headline"],
                    "Protagonists (Ground Truth)": ", ".join(truth_protagonists),
                    "Headline (Prediction)": prediction["headline"],
                    "Protagonists (Prediction)": ", ".join(prediction_protagonists),
                    "Headline Similarity (%)": headline_similarity,
                    "Protagonists Similarity (%)": protagonists_similarity,
                }
            )

    logger.info(f"Evaluation completed. Results saved to: {EVALUATION_RESULTS_PATH}")
