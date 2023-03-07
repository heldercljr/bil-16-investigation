# Python PDF Reading Libraries

Exemplos de scripts em Python em diferentes bibliotecas que extraem informações de um PDF específico (DASN - Documento de Arrecadação do Simples Nacional).
---
### Abaixo estão os exemplos em diferentes bibliotecas e uma análise a respeito delas.
O Ranking leva em consideração o quão bem apresentados estão os dados brutos e se para o exemplo citado a biblioteca se saiu bem.
|Ranking|Biblioteca|Funcionou|Observações|
|-------|----------|---------|-----------|
|1|[`PyMuPDF`](/pymupdf_.py)|Sim|Possui desempenho semelhante às demais, e apresenta os dados de maneira ainda mais organizada do que utilizando pdfplumber tendo os mesmos benefícios.|
|2|[`pdfplumber`](/pdfplumber_.py)|Sim|Possui desempenho semelhante às demais, e apresenta os dados brutos de maneira ainda mais organizada para o arquivo citado no exemplo. Utilizá-la é ainda mais simples, tendo em vista que a codificação é automática e ela já se encarrega de abrir o arquivo por conta própria.|
|3|[`PyPDF2`](/pypdf2.py)|Sim|A extração dos valores é rápida, sendo apenas necessário fazer uma varredura prévia e manual dos dados para saber o índice em que cada um se encontra, e em alguns casos tratar a string.|
|4|[`pdfminer`](/pdfminer_.py)|Sim|O formato padrão de execução dessa biblioteca é via linha de comando, mas ainda assim foi possível executá-la dentro do script. Nela os dados parecem mais bem separados do que utilizando PyPDF4, e a codificação UTF-8 é padrão. O maior contraponto é o fato que como é necessário localizar o executável da biblioteca (pdf2txt.py), isso talvez se torne algo a ser configurado manualmente, dependendo do SO utilizado.|
|5|[`PyPDF4`](/pypdf4.py)|Sim|Semelhante a PyPDF2, mas para o arquivo citado ele não reconhece a codificação correta como UTF-8. Apesar de tudo ter funcionado isso pode ser um impecilho para outros arquivos que demandam extração de strings maiores.|
|6|[`pdfrw`](/pdfrw_.py)|Parcialmente|Essa é uma biblioteca muito poderosa, no entanto ela não foi capaz de transformar o PDF do exemplo em um texto legível. De alguma forma a string de saída parece estrar encriptada ou comprimida. Ao que se parece essa biblioteca tem uma curva de aprendizado para utilização muito maior que as anteriores.|
