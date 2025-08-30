import json
from pathlib import Path

INPUT_FILE = Path("L13709compilado.pdf_TEXT.txt")
OUTPUT_FILE = Path("lgpd_dataset.json")


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Arquivo de entrada não encontrado: {INPUT_FILE.resolve()}"
        )

    text = INPUT_FILE.read_text(encoding="utf-8")

    # Dataset no formato esperado pelo DocETL: lista de objetos com chave "src"
    data = [{"src": text}]

    OUTPUT_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        f"OK: dataset gerado em {OUTPUT_FILE.resolve()} com {len(data)} documento(s)."
    )


if __name__ == "__main__":
    main()
