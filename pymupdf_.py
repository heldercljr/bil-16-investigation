import fitz
import re

from report import Report

# Nome do documento de onde virão os dados a serem extraídos

filename = "conta4.pdf"

# Abertura do documento pela própria biblioteca

with fitz.open(filename) as conta:

    # Extração do texto da primeira página

    text = conta[0].get_text()

# Separação do texto em linhas

lines = text.split("\n")

# Lista com a composição do documento:

lista = lines[lines.index("Composição do Documento de Arrecadação") + 1:lines.index("Totais"):1]
lista = [lista[i-1] for i in range(1, len(lista)) if lista[i-1].isupper() or re.match(r'\d+(,\d{2})', lista[i])]
lista = [{"denominacao": lista[i], "valor": lista[i+1]} for i in range(0, len(lista), 2)]

# Objeto responsável pela exportação dos dados

report = Report(
    lines[2],
    lines[12],
    lines[9],
    "".join(lines[-20:-16:1]).replace(" ", ""),
    lines[-15],
	lista
)

# Exportação do relatório para um arquivo JSON

report.to_json()
