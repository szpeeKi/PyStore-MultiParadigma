class Cliente:
    def __init__(self, cpf, nome, telefone, endereco_entrega):
        # Atributos privados conforme encapsulamento
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._endereco_entrega = endereco_entrega

    # Getters e Setters (Encapsulamento)
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_cpf(self):
        return self._cpf
    
    # O PDF pede um método toString (no Python é __str__) [cite: 52]
    def __str__(self):
        return f"Cliente: {self._nome} | CPF: {self._cpf} | Entrega: {self._endereco_entrega}"