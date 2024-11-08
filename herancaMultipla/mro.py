"""
Aqui está um exemplo de herança múltipla em um cenário mais
elaborado usando carros, onde explicaremos o conceito
de MRO (Method Resolution Order).

O MRO é a ordem na qual Python procura métodos em uma
hierarquia de classes quando múltiplas classes estão envolvidas.
Isso é especialmente importante em herança múltipla, onde métodos
e atributos podem existir em várias classes.

Exemplo de Herança Múltipla: Carro
Vamos criar uma hierarquia de classes para carros, onde:

Veiculo: Classe base para veículos, contendo atributos gerais como marca e modelo.
Combustao: Classe que adiciona métodos para veículos movidos a combustão (por exemplo, gasolina).
Eletrico: Classe que adiciona métodos para veículos elétricos.
CarroHibrido: Classe que herda de Combustao e Eletrico, combinando
comportamentos de carros movidos a gasolina e elétricos.
"""

class Veiculo:
    """
    Classe base que representa um veículo.
    """
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def info_veiculo(self):
        print(f"Veículo: {self.marca} {self.modelo}")

class Combustao(Veiculo):
    """
    Classe para veículos a combustão.
    """
    def __init__(self, marca: str, modelo: str, capacidade_tanque: int):
        super().__init__(marca, modelo)
        self.capacidade_tanque = capacidade_tanque
        self.nivel_combustivel = 0  # Inicialmente o tanque está vazio

    def abastecer(self, litros: int):
        if litros + self.nivel_combustivel <= self.capacidade_tanque:
            self.nivel_combustivel += litros
            print(f"Abastecido com {litros} litros. Nível atual: {self.nivel_combustivel} litros.")
        else:
            print("Não cabe tanto combustível no tanque.")

    def dirigir(self):
        if self.nivel_combustivel > 0:
            print(f"Dirigindo o {self.marca} {self.modelo} usando combustível.")
            self.nivel_combustivel -= 1
        else:
            print("Sem combustível! Abasteça para dirigir.")

class Eletrico(Veiculo):
    """
    Classe para veículos elétricos.
    """
    def __init__(self, marca: str, modelo: str, capacidade_bateria: int):
        super().__init__(marca, modelo)
        self.capacidade_bateria = capacidade_bateria
        self.nivel_bateria = 0  # Inicialmente a bateria está descarregada

    def carregar(self, kwh: int):
        if kwh + self.nivel_bateria <= self.capacidade_bateria:
            self.nivel_bateria += kwh
            print(f"Bateria carregada com {kwh} kWh. Nível atual: {self.nivel_bateria} kWh.")
        else:
            print("Não cabe tanta carga na bateria.")

    def dirigir(self):
        if self.nivel_bateria > 0:
            print(f"Dirigindo o {self.marca} {self.modelo} usando eletricidade.")
            self.nivel_bateria -= 1
        else:
            print("Bateria descarregada! Carregue para dirigir.")

class CarroHibrido(Combustao, Eletrico):
    """
    Classe para veículos híbridos, combinando combustão e eletricidade.
    """
    def __init__(self, marca: str, modelo: str, capacidade_tanque: int, capacidade_bateria: int):
        # Inicializa tanto Combustao quanto Eletrico
        Combustao.__init__(self, marca, modelo, capacidade_tanque)
        Eletrico.__init__(self, marca, modelo, capacidade_bateria)

    def dirigir(self):
        if self.nivel_combustivel > 0:
            # Usa combustível se disponível
            Combustao.dirigir(self)
        elif self.nivel_bateria > 0:
            # Se não houver combustível, usa eletricidade
            Eletrico.dirigir(self)
        else:
            print("Sem combustível e sem bateria! Impossível dirigir.")

# Exemplo de uso
carro_hibrido = CarroHibrido("Toyota", "Prius", 40, 100)

# Abastecendo e carregando o carro híbrido
carro_hibrido.abastecer(20)  # Combustível
carro_hibrido.carregar(50)   # Eletricidade

# Dirigindo o carro híbrido
carro_hibrido.dirigir()  # Usa combustível
carro_hibrido.dirigir()  # Continua usando combustível
