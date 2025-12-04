from models.Produto import Produto
class ProdutoFisico(Produto):
    def __init__(self, codigo, descricao, preco, quantidadeEstoque, peso, altura, largura, profundidade):
        super().__init__(codigo, descricao, preco, quantidadeEstoque)
        self._peso = peso
        self._altura = altura
        self._largura = largura
        self._profundidade = profundidade