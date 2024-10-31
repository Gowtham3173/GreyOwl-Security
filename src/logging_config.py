import logging

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,  # Default level
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/model_logs.log"),
        logging.StreamHandler()
    ]
)

# Function to set logging level dynamically
def set_logging_level(level_name):
    level = getattr(logging, level_name.upper(), logging.INFO)
    logging.getLogger().setLevel(level)
    logging.info(f"Logging level set to {level_name.upper()}")
