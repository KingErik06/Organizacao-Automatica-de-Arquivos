from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "data" / "input"

def organizar_arquivos():
    for item in INPUT_DIR.iterdir():
        if item.is_file():
            print(item.name)


if __name__ == "__main__":
    organizar_arquivos()