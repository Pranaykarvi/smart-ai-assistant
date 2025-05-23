# utils/helper_functions.py

import json
import logging
from pathlib import Path

def load_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to load JSON from {filepath}: {e}")
        return None

def save_json_file(filepath, data):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        logging.error(f"Failed to save JSON to {filepath}: {e}")
        return False

def clean_text(text):
    return text.strip().lower()

def log_message(msg):
    logging.info(msg)

# helper.py

import re

def normalize_command(command: str) -> str:
    command = command.lower().strip()

    # Preserve patterns like "open X and search for Y"
    if "open" in command and "search for" in command:
        return command

    # Preserve "search X on Y"
    if re.search(r"search .+ on .+", command):
        return command

    # Handle slash replacement
    command = command.replace(" slash ", "/")
    
    # Basic cleanup
    command = re.sub(r'[^\w\s./:-]', '', command)
    command = re.sub(r'\s+', ' ', command)

    return command.strip()



