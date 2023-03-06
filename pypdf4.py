import PyPDF4

with open("conta.pdf", mode="rb") as conta:
    pdf = PyPDF4.PdfFileReader(conta)

    page1 = pdf.getPage(0)

    text = page1.extractText()

    print(text)

    lines = text.split("\n")

    for line in lines:
        if "R$" in line:
            total = line.split(":")[-1].strip()
            break
