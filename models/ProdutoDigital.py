from models.Produto import Produto

class ProdutoDigital(Produto):
    def __init__(self, codigo, descricao, preco, quantidadeEstoque, tamanhoArquivoMB, formatoArquivo):
        super().__init__(codigo, descricao, preco, quantidadeEstoque)
        self._tamanhoArquivoMB = tamanhoArquivoMB
        self._formatoArquivo = formatoArquivo

    def getTamanhoArquivoMB(self):
        return self._tamanhoArquivoMB
    def setTamanhoArquivoMB(self, tamanhoArquivoMB):
        self._tamanhoArquivoMB = tamanhoArquivoMB

    def getFormatoArquivo(self):
        return self._formatoArquivo
    def setFormatoArquivo(self, formatoArquivo):
        self._formatoArquivo = formatoArquivo

    def calcular_valor_final(self, quantidade):
        valor_base = super().calcular_valor_final(quantidade)
        return valor_base