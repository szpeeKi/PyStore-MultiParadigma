class ItemCarrinho:
    def __init__(self, produto, quantidade):
        self._produto = produto
        self._quantidade = quantidade

    def getProduto(self):
        return self._produto
    def setProduto(self, produto):
        self._produto = produto

    def getQuantidade(self):
        return self._quantidade
    def setQuantidade(self, quantidade):
        self._quantidade = quantidade
    
    def calcular_valor_total(self):
        return self._produto.calcular_valor_final(self._quantidade)