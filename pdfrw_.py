import pdfrw

# Nome do documento de onde virão os dados a serem extraídos

filename = "conta3.pdf"

# Leitura do arquivo pela biblioteca

pdf = pdfrw.PdfReader(filename)

# Seleção da primeira página do documento

text = pdf.getPage(0).Contents.stream

# Demonstração dos dados

print(text)
