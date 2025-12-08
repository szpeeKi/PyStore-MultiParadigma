class ItemCarrinho:
    """
    Representa um item individual dentro do carrinho de compras.
    
    Conceito de POO: COMPOSIÇÃO/ASSOCIAÇÃO.
    Esta classe atua como um wrapper que conecta um objeto 'Produto' 
    a uma quantidade específica.
    """
    
    def __init__(self, produto, quantidade):
        """
        Inicializa o item do carrinho com atributos protegidos.

        Args:
            produto: Instância de Produto (Físico ou Digital).
            quantidade: Inteiro representando quantos itens deste produto serão levados.
        """
        self._produto = produto
        self._quantidade = quantidade

    def getProduto(self):
        """
        Retorna o objeto Produto associado a este item.
        """
        return self._produto

    def setProduto(self, produto):
        """
        Define ou substitui o produto deste item.

        Args:
            produto: O novo objeto Produto a ser associado.
        """
        self._produto = produto

    def getQuantidade(self):
        """
        Retorna a quantidade atual do item.
        """
        return self._quantidade

    def setQuantidade(self, quantidade):
        """
        Atualiza a quantidade do item.

        Args:
            quantidade: O novo valor inteiro da quantidade.
        """
        self._quantidade = quantidade
    
    def calcular_valor_total(self):
        """
        Calcula o subtotal deste item.

        A lógica delega o cálculo para o método do próprio produto,
        permitindo que o polimorfismo do Produto (Físico vs Digital)
        defina como o preço é calculado com base na quantidade.
        """
        return self._produto.calcular_valor_final(self._quantidade)