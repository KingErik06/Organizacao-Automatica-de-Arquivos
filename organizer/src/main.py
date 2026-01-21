from pathlib import Path
import shutil

def organizar_arquivos(pasta: Path) -> None:
    """Organiza arquivos em subpastas por extensão."""
    for arquivo in pasta.iterdir():
        if arquivo.is_file():
            mover_arquivo(arquivo)


def mover_arquivo(arquivo: Path) -> None:
    """Move o arquivo para uma pasta baseada na extensão."""
    if not arquivo.suffix:
        return

    pasta_destino = arquivo.parent / arquivo.suffix[1:].upper()
    pasta_destino.mkdir(exist_ok=True)
    shutil.move(arquivo, pasta_destino / arquivo.name)


def main():
    pasta_input = Path("data/input")
    organizar_arquivos(pasta_input)


if __name__ == "__main__":
    main()