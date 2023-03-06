import PyPDF2

with open("conta2.pdf", "rb") as conta:
    pdf = PyPDF2.PdfReader(conta)

    page1 = pdf.pages[0]

    text = page1.extract_text()

    lines = text.split("\n")

    for line in lines:
        if "TOTAL: " in line:
            total = line.split()[2].replace("-", "")
            break

    print(f"R$ " + total)
