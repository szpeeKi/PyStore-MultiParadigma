from models.Produto import Produto
class ProdutoFisico(Produto):
    def __init__(self, codigo, descricao, preco, quantidadeEstoque, peso, altura, largura, profundidade,frete):
        super().__init__(codigo, descricao, preco, quantidadeEstoque)
        self._peso = peso
        self._altura = altura
        self._largura = largura
        self._profundidade = profundidade
        self._frete = frete

    def calcular_valor_final(self, quantidade):
        return super().calcular_valor_final(quantidade) + self._frete