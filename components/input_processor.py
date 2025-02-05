# INPUT_PROCESSOR.PY:

import os
import logging

logger = logging.getLogger(__name__)


class InputProcessor:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def get_all_image_paths(self) -> list[str]:
        """Returns all file paths in the folder."""
        image_paths = [
            os.path.join(self.folder_path, file)
            for file in os.listdir(self.folder_path)
        ]
        logger.info(f"Found {len(image_paths)} covers for processing.")
        return image_paths

    def get_image_id(self, image_path: str) -> str:
        """Extracts the ID from the image file name."""
        return os.path.splitext(os.path.basename(image_path))[0]
