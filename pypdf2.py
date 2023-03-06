import PyPDF2
import re

# Nome do documento de onde virão os dados a serem extraídos

filename = "conta3.pdf"

# Abertura do documento

with open(filename, "rb") as conta:

    # Leitura do arquivo pela biblioteca

    pdf = PyPDF2.PdfReader(conta)

    # Seleção da página do documento

    page1 = pdf.pages[0]

    # Extração do texto da página

    text = page1.extract_text()

    # Separação do texto por linha

    lines = text.split("\n")

    # Dicionário responsável pela exportação dos dados

    report = {
        "valor": lines[7].split()[0],
        "data_de_vencimento": lines[5].split()[0],
        "codigo_de_barras": re.sub(r'\D', '', lines[-8]),
        "tipo_do_documento": lines[-7].strip()
    }

    # Demonstração dos dados

    print(report)
