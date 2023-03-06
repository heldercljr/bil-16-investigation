import PyPDF2
import re

with open("conta3.pdf", "rb") as conta:
    pdf = PyPDF2.PdfReader(conta)

    page1 = pdf.pages[0]

    text = page1.extract_text()

    lines = text.split("\n")

    report = {
        "valor": lines[7].split()[0],
        "data_de_vencimento": lines[5].split()[0],
        "codigo_de_barras": re.sub(r'\D', '', lines[-8]),
        "tipo_do_documento": lines[-7].strip()
    }

    print(report)
