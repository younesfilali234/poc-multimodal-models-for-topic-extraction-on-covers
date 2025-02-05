import logging
from components.database_handler import DatabaseHandler
from components.input_processor import InputProcessor
from components.inference_handler import InferenceHandler
from components.output_processor import OutputProcessor
from components.evaluator import evaluate_predictions
from settings import MODEL_NAME, SEED, IMAGE_FOLDER, PREDICTIONS_DB_PATH, PROMPT
from typing import List, Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def initialize_components() -> Tuple[InputProcessor, InferenceHandler, DatabaseHandler]:
    """Initializes and returns the necessary components for the pipeline."""
    return (
        InputProcessor(folder_path=IMAGE_FOLDER),
        InferenceHandler(model_name=MODEL_NAME, seed=SEED),
        DatabaseHandler(db_path=PREDICTIONS_DB_PATH),
    )


def process_images(input_processor: InputProcessor) -> List[Tuple[str, str]]:
    """Processes all input images and returns a list of image paths and IDs."""
    image_paths = input_processor.get_all_image_paths()
    return [(path, input_processor.get_image_id(path)) for path in image_paths]


def run_inference_and_save(
    image_path: str,
    image_id: str,
    inference_handler: InferenceHandler,
    database_handler: DatabaseHandler,
) -> None:
    """Runs inference on the image, processes the output, and saves the prediction to the database."""
    output = inference_handler.run_inference(image_path=image_path, prompt=PROMPT)
    structured_output = OutputProcessor.process_inference_output(
        output=output, image_id=image_id
    )
    database_handler.save_data("predictions", structured_output)


def main() -> None:
    """Main pipeline for processing multiple images, running inference, saving results, and evaluating predictions."""
    logger.info("Pipeline started.")
    try:
        input_processor, inference_handler, database_handler = initialize_components()
        images = process_images(input_processor)
        for image_path, image_id in images:
            run_inference_and_save(
                image_path, image_id, inference_handler, database_handler
            )
        evaluate_predictions()
        logger.info("Pipeline successfully completed.")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")


if __name__ == "__main__":
    main()
