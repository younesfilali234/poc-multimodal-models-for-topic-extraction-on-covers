# OUTPUT_PROCESSOR.PY:

import json
import logging

logger = logging.getLogger(__name__)


class OutputProcessor:
    @staticmethod
    def process_inference_output(output: str, image_id: str) -> dict:
        """Processes and prepares inference output for storage."""
        try:
            output_dict = json.loads(output)
            return {
                "id": image_id,
                "headline": output_dict.get("headline", ""),
                "protagonists": output_dict.get("protagonists", []),
            }
        except json.JSONDecodeError as e:
            logger.error(
                f"Invalid JSON for image {image_id}: {e}. Returning default values."
            )
            return {"id": image_id, "headline": "", "protagonists": []}
