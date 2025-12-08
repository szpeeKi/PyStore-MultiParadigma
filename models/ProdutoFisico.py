from models.Produto import Produto

class ProdutoFisico(Produto):
    """
    Representa um produto físico (ex: Livro impresso) que requer logística de entrega.

    Conceito de POO: HERANÇA.
    Estende a classe 'Produto' adicionando atributos físicos (dimensões, peso)
    e custos logísticos (frete).
    """

    def __init__(self, codigo, descricao, preco, quantidadeEstoque, peso, altura, largura, profundidade, frete, tipo="Físico"):
        """
        Inicializa o produto físico.

        Args:
            codigo, descricao, preco, quantidadeEstoque: Repassados para a superclasse Produto.
            peso, altura, largura, profundidade: Dimensões físicas do item.
            frete: Valor monetário do custo de envio.
        """
        super().__init__(codigo, descricao, preco, quantidadeEstoque)
        self._peso = peso
        self._altura = altura
        self._largura = largura
        self._profundidade = profundidade
        self._frete = frete
        self._tipo = tipo

    def to_dict(self):
        # Pega os dados básicos da classe pai (Produto)
        data = super().to_dict()
        # Adiciona os dados específicos desta classe
        data.update({
            "peso": self._peso,
            "altura": self._altura,
            "largura": self._largura,
            "profundidade": self._profundidade,
            "frete": self._frete
        })
        return data  

    def calcular_valor_final(self, quantidade):
        """
        Calcula o preço final considerando o custo de envio.

        Conceito de POO: POLIMORFISMO.
        Sobrescreve o método da classe pai (Produto) para alterar o comportamento padrão.
        
        Lógica aplicada:
        1. Chama a lógica padrão (Preço x Quantidade) via super().
        2. Soma o valor do frete ao total.
        """
        return super().calcular_valor_final(quantidade) + self._frete