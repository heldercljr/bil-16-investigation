import fitz

from report import Report

# Nome do documento de onde virão os dados a serem extraídos

filename = "conta3.pdf"

# Abertura do documento pela própria biblioteca

with fitz.open(filename) as conta:

    # Extração do texto da primeira página

    text = conta[0].get_text()

# Separação do texto em linhas

lines = text.split("\n")

# Objeto responsável pela exportação dos dados

report = Report(
    lines[2],
    lines[12],
    lines[9],
    "".join(lines[-20:-16:1]).replace(" ", ""),
    lines[-15],
    lines[24:52:1]
)

# Exportação do relatório para um arquivo JSON

report.to_json()
