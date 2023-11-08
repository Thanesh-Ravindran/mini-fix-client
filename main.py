# main.py

import logging

logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
from src.utils import load_config
from src.fix_client import FixClient

if __name__ == "__main__":
    config = load_config("config/config.json")

    client = FixClient(config)
    try:
        logging.info("Application started")
        client.run()

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
