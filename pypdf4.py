import PyPDF4
import re

with open("conta4.pdf", "rb") as conta:
    pdf = PyPDF4.PdfFileReader(conta)
    
    page1 = pdf.getPage(0)

    text = page1.extractText()

    lines = text.split("\n")

    report = {
        "valor": lines[12],
        "data_de_vencimento": lines[9],
        "codigo_de_barras": re.sub(r'\D', '', lines[-17]) + lines[-16],
        "tipo_do_documento": lines[-14].replace("!", "ã")
    }

    print(report)
