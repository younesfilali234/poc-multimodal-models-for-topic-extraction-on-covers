# INFERENCE_HANDLER.PY:

import logging
from ollama import chat

logger = logging.getLogger(__name__)


class InferenceHandler:
    def __init__(self, model_name: str, seed: int):
        self.model_name = model_name
        self.seed = seed

    def run_inference(self, image_path: str, prompt: str) -> str | None:
        """Runs inference on the given image with the specified prompt."""
        try:
            response = chat(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt, "images": [image_path]}],
                options={"seed": self.seed},
            )
            logger.info(f"Inference successful for {image_path}")
            return response.message.content
        except Exception as e:
            logger.error(f"Inference failed for {image_path}: {e}")
            return "{}"
