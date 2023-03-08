import json

class Report:

    def __init__(self, cnpj, valor, data_de_vencimento, codigo_de_barras, tipo_do_documento, composicao_do_documento):
        self.cnpj = cnpj
        self.valor = valor
        self.data_de_vencimento = data_de_vencimento
        self.codigo_de_barras = codigo_de_barras
        self.tipo_do_documento = tipo_do_documento
        self.composicao_do_documento = composicao_do_documento

    def __str__(self):
        return json.dumps(self, ensure_ascii=False).encode("utf-8")
