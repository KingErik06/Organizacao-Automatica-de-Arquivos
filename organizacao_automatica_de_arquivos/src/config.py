from pathlib import Path

BASE_DIR = Path(__file__).resolve.parent.parent

DATA_INPUT = BASE_DIR / "data" / "input"
DATA_OUTPUT = BASE_DIR / "data" / "output"
LOGS_DIR = BASE_DIR / "logs"