import pytesseract
import pdf2image

from PIL import Image

pdf = pdf2image.convert_from_path("conta.pdf")

img = Image.open(pdf)

text = pytesseract.image_to_string(img)

print(text)
