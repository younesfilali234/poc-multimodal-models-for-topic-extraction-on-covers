MODEL_NAME = "llama3.2-vision"
SEED = 48

IMAGE_FOLDER = "data/covers"
PREDICTIONS_DB_PATH = "data/databases/predictions.db"
GROUND_TRUTH_DB_PATH = "data/databases/ground_truth.db"
EVALUATION_RESULTS_PATH = "data/evaluation/results.csv"

PROMPT = (
    "Analyze the given magazine cover. Identify the main headline and the protagonists associated with it. "
    "Only extract names that are explicitly mentioned on the cover and are directly related to the headline. "
    "The output must strictly follow this JSON format: "
    '{"headline": "<string>", "protagonists": ["<string1>", "<string2>", "..."]}'
    'Ensure that "headline" is a single string and "protagonists" is a list of strings, even if there is only one protagonist. '
    "Do not add any other text, comments, or explanation outside the JSON output."
)
