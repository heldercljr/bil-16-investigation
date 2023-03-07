import fitz

# Nome do documento de onde virão os dados a serem extraídos

filename = "conta3.pdf"

# Abertura do documento pela própria biblioteca

with fitz.open(filename) as conta:

	# Extração do texto da primeira página

	text = conta[0].get_text()

	# Separação do texto em linhas

	lines = text.split("\n")

	# Dicionário responsável pela exportação dos dados

	report = {
		"valor": lines[12],
		"data_de_vencimento": lines[9],
		"codigo_de_barras": "".join(lines[-20:-16:1]).replace(" ", ""),
		"tipo_do_documento": lines[-15]
	}

	# Demonstração dos dados

	print(report)