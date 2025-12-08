class Carrinho:
    """
    Gerencia as operações de adição e remoção de produtos no processo de compra.
    """
    
    def __init__(self):
        """Inicializa um novo carrinho com uma lista vazia de itens."""
        self._itens = []

    def adicionar_item(self, item):
        """
        Adiciona um item ao carrinho.

        Args:
            item: O objeto (ItemCarrinho) a ser adicionado.
        """
        self._itens.append(item)

    def limpar_carrinho(self, item):
        """
        Remove um item do carrinho, se ele existir na lista.
        
        Args:
            item: O objeto a ser removido.
        """
        if item in self._itens:
            self._itens.remove(item)

    def listar_itens(self):
        """
        Retorna todos os itens presentes no carrinho.

        Returns:
            list: Lista contendo os objetos adicionados.
        """
        return self._itens