# utils.py

import os
from datetime import datetime


def log_event(file_path, message):
    # Fix: correct parameter order

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    directory = os.path.dirname(file_path)

    # Fix: avoid empty directory error
    if directory != "":
        os.makedirs(directory, exist_ok=True)

    with open(file_path, "a") as f:
        f.write(log_entry)

    print(log_entry.strip())


def generate_filename(prefix="violation", extension="jpg"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"


def ensure_directory(path):
    os.makedirs(path, exist_ok=True)