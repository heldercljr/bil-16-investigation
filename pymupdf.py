import fitz

with fitz.open("conta.pdf") as conta:
	page1 = conta[0]

	print(page1.strip())