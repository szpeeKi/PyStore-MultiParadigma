from models.Produto import Produto

class ProdutoDigital(Produto):
    """
    Representa um produto digital (ex: E-book) vendido na loja.

    Conceito de POO: HERANÇA.
    Esta classe estende (herda de) 'Produto', aproveitando seus atributos
    (código, preço, etc.) e adicionando especificidades de arquivos digitais.
    """

    def __init__(self, codigo, descricao, preco, quantidadeEstoque, tamanhoArquivoMB, formatoArquivo, tipo="Digital"):
        """
        Inicializa o produto digital.

        Usa 'super().__init__' para garantir que a lógica de inicialização 
        da classe pai (Produto) seja executada antes de definir os atributos específicos.
        """
        super().__init__(codigo, descricao, preco, quantidadeEstoque)
        self._tamanhoArquivoMB = tamanhoArquivoMB
        self._formatoArquivo = formatoArquivo
        self.tipo = tipo
    
    def to_dict(self):
        return super().to_dict()

    # --- Getters e Setters Específicos ---

    def getTamanhoArquivoMB(self):
        """Retorna o tamanho do arquivo em Megabytes."""
        return self._tamanhoArquivoMB

    def setTamanhoArquivoMB(self, tamanhoArquivoMB):
        """Define o tamanho do arquivo."""
        self._tamanhoArquivoMB = tamanhoArquivoMB

    def getFormatoArquivo(self):
        """Retorna o formato do arquivo (ex: PDF, EPUB)."""
        return self._formatoArquivo

    def setFormatoArquivo(self, formatoArquivo):
        """Define o formato do arquivo."""
        self._formatoArquivo = formatoArquivo

    def calcular_valor_final(self, quantidade):
        """
        Calcula o preço final para produtos digitais.

        Conceito de POO: POLIMORFISMO (Sobrescrita de Método).
        Este método sobrescreve a versão da classe pai. 
        
        Neste caso específico, ele opta por manter a lógica base (chamando super()),
        o que faz sentido para produtos digitais que geralmente não possuem frete 
        adicional, diferenciando-se dos produtos físicos.
        """
        valor_base = super().calcular_valor_final(quantidade)
        return valor_base