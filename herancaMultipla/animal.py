"""
Exemplo de Herança Múltipla
Vamos definir as seguintes classes:

Animal: Classe base para todos os animais.
Aviar: Classe que representa animais que podem voar.
Nadar: Classe que representa animais que podem nadar.
Pato: Classe que herda de Animal, Aviar, e Nadar, representando um pato que pode voar e nadar.
"""

class Animal:
    """
    Classe base para todos os animais.
    """
    def __init__(self, nome: str):
        self.nome = nome

    def fazer_som(self):
        raise NotImplementedError("Subclasse deve implementar este método")

class Aviar:
    """
    Classe que representa animais que podem voar.
    """
    def voar(self):
        print(f"{self.nome} está voando.")

class Nadar:
    """
    Classe que representa animais que podem nadar.
    """
    def nadar(self):
        print(f"{self.nome} está nadando.")

class Pato(Animal, Aviar, Nadar):
    """
    Classe que representa um pato, que pode voar e nadar.
    """
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print(f"{self.nome} faz quack!")

# Criando um pato
pato = Pato("Donald")

# Chamando métodos disponíveis através da herança múltipla
pato.fazer_som()  # Método da classe Animal
pato.voar()       # Método da classe Aviar
pato.nadar()      # Método da classe Nadar
