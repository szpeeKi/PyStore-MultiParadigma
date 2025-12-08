class Cliente:
    """
    Representa um cliente da loja.
    
    Demonstra o conceito de ENCAPSULAMENTO ao utilizar atributos protegidos
    (iniciados com '_') acessíveis via métodos Getters e Setters.
    """

    def __init__(self, cpf, nome, telefone, endereco_entrega):
        """
        Inicializa o cliente definindo seus atributos como protegidos.

        Args:
            cpf: CPF do cliente.
            nome: Nome completo.
            telefone: Número de telefone para contato.
            endereco_entrega: Endereço para envio de produtos físicos.
        """
        # Atributos privados conforme encapsulamento
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._endereco_entrega = endereco_entrega

    # Getters e Setters (Encapsulamento)
    def get_nome(self):
        """
        Retorna o nome atual do cliente.
        """
        return self._nome

    def set_nome(self, nome):
        """
        Atualiza o nome do cliente.

        Args:
            nome: O novo nome a ser atribuído.
        """
        self._nome = nome

    def get_cpf(self):
        """
        Retorna o CPF do cliente.
        """
        return self._cpf
    
    # O PDF pede um método toString (no Python é __str__)
    def __str__(self):
        """
        Retorna uma representação legível do objeto Cliente em formato de string.
        """
        return f"Cliente: {self._nome} | CPF: {self._cpf} | Entrega: {self._endereco_entrega}"