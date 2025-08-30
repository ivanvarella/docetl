from docling.document_converter import DocumentConverter
import os
import unicodedata
import json
from pathlib import Path


# Normalizar nomes para evitar problemas com caracteres
def normalize_filename(filename):
    return unicodedata.normalize("NFC", filename)


def main():
    # Caminhos base
    base_path = os.path.join(os.getcwd(), "dados_fonte")
    pdfs_path = os.path.join(base_path, "pdfs")
    textos_path = os.path.join(base_path, "textos")

    # Garantir que a pasta de textos existe
    os.makedirs(textos_path, exist_ok=True)

    target_name = "L13709compilado.pdf"
    normalized_target = normalize_filename(target_name)

    # Procurar o arquivo na pasta de PDFs
    for filename in os.listdir(pdfs_path):
        normalized_filename = normalize_filename(filename)
        if normalized_filename == normalized_target:
            pdf_path = os.path.join(pdfs_path, filename)
            print(f"Arquivo encontrado: {pdf_path}\n\n")
            break
    else:
        raise FileNotFoundError(
            f"Arquivo '{target_name}' não encontrado em {pdfs_path}"
        )

    # Convertendo para texto usando Docling
    print("Convertendo PDF para texto usando Docling...")
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    text = result.document.export_to_text()

    # Salvando o arquivo TXT na pasta textos
    text_filename = target_name.replace(".pdf", "_TEXT.txt")
    text_path = os.path.join(textos_path, text_filename)

    try:
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Arquivo de texto salvo em: {text_path}\n")
    except Exception as e:
        print(f"Erro ao salvar o arquivo de texto: {e}\n")
        return

    # Criando o dataset JSON no formato esperado pelo DocETL
    print("Criando dataset JSON...")
    output_file = Path("lgpd_dataset.json")

    # Dataset no formato esperado pelo DocETL: lista de objetos com chave "src"
    data = [{"src": text}]

    try:
        output_file.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(
            f"OK: dataset gerado em {output_file.resolve()} com {len(data)} documento(s)."
        )
    except Exception as e:
        print(f"Erro ao salvar o dataset JSON: {e}\n")
        return


if __name__ == "__main__":
    main()
