"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.
"""

from datetime import datetime

class Pessoa:
    """
    Classe que representa uma pessoa, com propriedades para nome, data de nascimento e email.
    """
    def __init__(self, nome: str, data_nascimento: str, email: str):
        self._nome = nome
        self._data_nascimento = self._validar_data(data_nascimento)
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        if len(novo_nome) > 0:
            self._nome = novo_nome
        else:
            raise ValueError("O nome não pode ser vazio.")

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data: str):
        data_valida = self._validar_data(nova_data)
        if data_valida:
            self._data_nascimento = data_valida
        else:
            raise ValueError("Data de nascimento inválida.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email: str):
        if "@" in novo_email and "." in novo_email:
            self._email = novo_email
        else:
            raise ValueError("Email inválido.")


    def _validar_data(self, data: str) -> datetime:
        try:
            return datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data deve estar no formato DD/MM/YYYY.")

    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")
        print(f"Email: {self.email}")


julio = Pessoa("Julio", "30/11/1995", "jcbs3095@gmail.com")
julio.imprimir_dados()