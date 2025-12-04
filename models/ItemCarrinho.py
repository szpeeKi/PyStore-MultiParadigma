class itemCarrinho:
    def __init__(self, produto, quantidade):
        self._produto = produto
        self._quantidade = quantidade

    def getProduto(self):
        return self._produto    

    def getQuantidade(self):
        return self._quantidade