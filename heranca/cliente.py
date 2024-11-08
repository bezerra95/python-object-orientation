"""
Abstração: As classes abstraem o conceito de produtos, clientes e pedidos do mundo real.

Encapsulamento: Os atributos nome, preco, cpf, e itens estão encapsulados dentro das classes,
protegendo os dados e controlando o acesso através de métodos.

Objetos: As instâncias cliente1, produto1, produto2 e pedido1
são objetos das respectivas classes.

Herança: A classe ClienteVIP herda da classe Cliente.
Isso significa que ClienteVIP pode reutilizar todos os atributos
e métodos de Cliente e adicionar ou modificar comportamento, como o atributo desconto.
"""


class Cliente:
    """
    Classe que representa um cliente comum, usando propriedades para encapsulamento.
    """
    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = cpf

    # Propriedade para acessar o nome do cliente
    @property
    def nome(self):
        return self._nome

    # Propriedade setter para modificar o nome do cliente
    @nome.setter
    def nome(self, novo_nome: str):
        if len(novo_nome) > 0:  # Validação simples
            self._nome = novo_nome
        else:
            raise ValueError("O nome não pode ser vazio.")

    # Propriedade para acessar o CPF
    @property
    def cpf(self):
        return self._cpf

    def get_info(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"


class ClienteVIP(Cliente):
    """
    Classe que representa um cliente VIP com desconto especial.
    """
    def __init__(self, nome: str, cpf: str, desconto: float):
        super().__init__(nome, cpf)  # Reutiliza o construtor da classe base (Cliente)
        self._desconto = desconto

    @property
    def desconto(self):
        return self._desconto

    @desconto.setter
    def desconto(self, valor: float):
        if 0 <= valor <= 1:
            self._desconto = valor
        else:
            raise ValueError("O desconto deve estar entre 0 e 1.")

    def get_info(self):
        return f"{super().get_info()}, Cliente VIP com {self.desconto * 100}% de desconto"
