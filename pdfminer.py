import subprocess

# Nome do documento de onde virão os dados a serem extraídos

filename = "conta4.pdf"

# Execução do processo pdf2txt, que é como a biblioteca pdfminer é utilizada

result = subprocess.run(["pdf2txt.py", filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Extração do texto do PDF com a codificação em UTF-8 (Apesar de ser padrão no pdfminer)

text = result.stdout.decode("utf-8")

# Separação do texto por linha, excluindo aquelas vazias

lines = [s for s in text.split("\n") if s != ""]

# Dicionário responsável pela exportação dos dados

report = {
	"valor": lines[-2],
	"data_de_vencimento": lines[-3],
	"codigo_de_barras": "".join(lines[-20:-16:1]).replace(" ", ""),
	"tipo_do_documento": lines[-15]
}

# Demonstração dos dados

print(report)
