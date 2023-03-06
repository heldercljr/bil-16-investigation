import pdfplumber
import re

# Nome do documento de onde virão os dados a serem extraídos

filename = "conta3.pdf"

# Abertura do documento pela própria biblioteca

with pdfplumber.open(filename) as pdf:

	# Extração do texto da primeira página
	
	text = pdf.pages[0].extract_text()

	# Separação do texto em linhas

	lines = text.split("\n")

	# Dicionário responsável pela exportação dos dados

	report = {
		"valor": lines[9],
		"data_de_vencimento": lines[6],
		"codigo_de_barras": re.sub(r'\D', '', lines[-6]),
		"tipo_do_documento": lines[-5].replace(" Pague com o PIX", "")
	}

	# Demonstração dos dados

	print(report)