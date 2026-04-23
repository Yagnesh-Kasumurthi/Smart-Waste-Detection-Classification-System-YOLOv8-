# config.py

WASTE_CATEGORIES = {
    "bottle": "Plastic Waste",
    "cup": "Plastic Waste",
    "cell phone": "E-Waste",
    "banana": "Organic Waste",
    "apple": "Organic Waste",
    "book": "Paper Waste",
    "remote": "E-Waste",
    "laptop": "E-Waste"
}

ALLOWED_CLASSES = [
    "person",
    "bottle",
    "cup",
    "cell phone",
    "banana",
    "apple",
    "book",
    "remote",
    "laptop"
]

SAVE_PATH = "outputs/violations"
LOG_FILE = "outputs/logs.txt"

COLOR_PERSON = (255, 200, 0)
COLOR_WASTE = (0, 0, 255)
COLOR_INFO = (0, 255, 0)