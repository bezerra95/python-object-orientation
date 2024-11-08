"""
 2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
 a) armazenar_contato(contato: Contato);
 b) remover_contato(contato: Contato);
 c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
 d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
 e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice
"""


class Contato:
    """
    Classe que representa uma pessoa, com propriedades para nome, data de nascimento e email.
    """
    indice = 1

    def __init__(self, nome: str, data_nascimento: str, email: str):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._email = email
        self.indice = Contato.indice
        Contato.indice += 1

    # Getter para nome
    @property
    def nome(self):
        return self._nome

    # Getter para data de nascimento
    @property
    def data_nascimento(self):
        return self._data_nascimento

    # Getter para email
    @property
    def email(self):
        return self._email


class Agenda:
    def __init__(self):
        self._contatos = []

    def armazenar(self, contato: Contato):
        self._contatos.append(contato)
        #print(f"Contato armazenado: {contato.indice} {contato.nome}")

    def remover(self, id_contato: int):
        for contato in self._contatos:
            if contato.indice == id_contato:
                self._contatos.remove(contato)
                print(f"Contato removido: {contato.indice} {contato.nome}")
                return
        print(f"Contato com índice {id_contato} não encontrado.")

    def buscar(self, nome: str):
        for contato in self._contatos:
            if contato.nome == nome:
                print(f"Contato buscado: {contato.indice} {contato.nome}")
                return
            print(f"Contato com nome {nome} não encontrado.")

    def imprimir_lista_de_contatos(self):
        print("Lista de contatos:")
        for contato in self._contatos:
            print(f"{contato.indice}: {contato.nome} - {contato.email}")

    def imprimir_contato(self, id: int):
        for contato in self._contatos:
            if contato.indice == id:
                self._contatos.remove(contato)
                print(f"Contato: {contato.indice} {contato.nome}")
                return
        print(f"Contato com índice {id} não encontrado.")


ana = Contato("Ana Maria", "12/05/1990", "ana.maria@example.com")
carlos = Contato("Carlos Souza", "07/08/1985", "carlos.souza@example.com")
mariana = Contato("Mariana Oliveira", "15/03/1992", "mariana.oliveira@example.com")
lucas = Contato("Lucas Pereira", "22/09/1988", "lucas.pereira@example.com")

agenda = Agenda()

agenda.armazenar(ana)
agenda.armazenar(carlos)
agenda.armazenar(mariana)
agenda.armazenar(lucas)

print("Respostas:")
print()
agenda.remover(1)
print()
agenda.buscar("Carlos Souza")
print()
agenda.imprimir_lista_de_contatos()
print()
agenda.imprimir_contato(3)
