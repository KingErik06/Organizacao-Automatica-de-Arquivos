from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "data" / "input"

def organizar_arquivos():
    for item in INPUT_DIR.iterdir():
        if not item.is_file():
            continue

        extensao = item.suffix.lower()

        if not extensao:
            continue

        extensao = extensao.replace(".", "")
        pasta_destino = INPUT_DIR / extensao

        if not pasta_destino.exists():
            pasta_destino.mkdir()

        destino = pasta_destino / item.name
        print(f"Movendo {item.name} -> {pasta_destino.name}/")

        item.rename(destino)

if __name__ == "__main__":
    organizar_arquivos()