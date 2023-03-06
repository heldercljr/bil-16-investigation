import PyPDF4
import re

# Abertura do documento

with open("conta4.pdf", "rb") as conta:

    # Leitura do arquivo pela biblioteca

    pdf = PyPDF4.PdfFileReader(conta)

    # Seleção da página do documento

    page1 = pdf.getPage(0)

    # Extração do texto da página

    text = page1.extractText()

    # Separação do texto por linha

    lines = text.split("\n")

    # Dicionário responsável pela exportação dos dados

    report = {
        "valor": lines[12],
        "data_de_vencimento": lines[9],
        "codigo_de_barras": re.sub(r'\D', '', lines[-17]) + lines[-16],
        "tipo_do_documento": lines[-14].replace("!", "ã")
    }

    # Demonstração dos dados

    print(report)
