# src/utils.py
# load a JSON config file, return its contents as dict
# handle file not found and JSON decoding errors

import json
import logging

logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def load_config(config):
    try:
        with open(config, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Config file not found: {config}")
        return {}
    except json.JSONDecodeError:
        logging.error(
            f"Failed to load configuration from: {config}. Invalid JSON format."
        )
        return {}
