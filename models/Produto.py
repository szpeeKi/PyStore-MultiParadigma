class Produto:
    def __init__(self, codigo, descricao, preco, quantidadeEstoque):
        self._codigo = codigo
        self._descricao = descricao
        self._preco = preco
        self._quantidadeEstoque = quantidadeEstoque

    def getCodigo(self):
        return self._codigo
    def setCodigo(self, codigo):
        self._codigo = codigo

    def getDescricao(self):
        return self._descricao
    def setDescricao(self, descricao):
        self._descricao = descricao 

    def getPreco(self):
        return self._preco
    def setPreco(self, preco):
        self._preco = preco

    def getQuantidadeEstoque(self):
        return self._quantidadeEstoque
    def setQuantidadeEstoque(self, quantidadeEstoque):
        self._quantidadeEstoque = quantidadeEstoque

    def calcular_valor_final(self, quantidade):
        return self._preco * quantidade
    
    def __str__(self):
        return f"{self._codigo} - {self._descricao} | R$ {self._preco:.2f}"