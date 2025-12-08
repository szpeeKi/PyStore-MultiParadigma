class Produto:
    """
    Classe Base (Superclasse) para todos os produtos da loja.

    Conceitos de POO:
    - ABSTRAÇÃO/HERANÇA: Serve de modelo genérico para tipos específicos (Físico/Digital).
    - ENCAPSULAMENTO: Atributos protegidos acessados via Getters e Setters.
    """

    def __init__(self, codigo, descricao, preco, quantidadeEstoque):
        """
        Inicializa um produto genérico.

        Args:
            codigo: Identificador único do produto.
            descricao: Nome ou descrição do produto.
            preco: Valor unitário base.
            quantidadeEstoque: Quantidade disponível.
        """
        self._codigo = codigo
        self._descricao = descricao
        self._preco = preco
        self._quantidadeEstoque = quantidadeEstoque

    # --- Getters e Setters (Encapsulamento) ---

    def getCodigo(self):
        """Retorna o código do produto."""
        return self._codigo

    def setCodigo(self, codigo):
        """Define o código do produto."""
        self._codigo = codigo

    def getDescricao(self):
        """Retorna a descrição do produto."""
        return self._descricao

    def setDescricao(self, descricao):
        """Define a descrição do produto."""
        self._descricao = descricao 

    def getPreco(self):
        """Retorna o preço unitário."""
        return self._preco

    def setPreco(self, preco):
        """Define o preço unitário."""
        self._preco = preco

    def getQuantidadeEstoque(self):
        """Retorna a quantidade atual em estoque."""
        return self._quantidadeEstoque

    def setQuantidadeEstoque(self, quantidadeEstoque):
        """Atualiza a quantidade em estoque."""
        self._quantidadeEstoque = quantidadeEstoque

    # --- Métodos de Negócio ---

    def calcular_valor_final(self, quantidade):
        """
        Calcula o valor total base para uma quantidade de itens.
        
        Nota sobre POLIMORFISMO:
        Nas subclasses (ProdutoFisico/ProdutoDigital), este método pode ser 
        sobrescrito (override) para incluir regras específicas, como frete ou descontos.
        """
        return self._preco * quantidade
    
    def __str__(self):
        """
        Retorna a representação textual do produto para exibição em menus e listas.
        """
        return f"{self._codigo} - {self._descricao} | R$ {self._preco:.2f}"