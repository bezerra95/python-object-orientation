"""
Poli -> Muitos
Morfismo -> Formas
Polimorfismo permite que objetos diferentes (Círculo, Quadrado, Triângulo)
usem o mesmo método (area()), cada um com seu próprio comportamento.
"""
import math

class Forma:
    """
    Classe base abstrata para formas geométricas.
    """
    def area(self):
        """
        Método que será sobrescrito pelas subclasses para calcular a área.
        """
        raise NotImplementedError("O método área deve ser implementado pelas subclasses")


class Circulo(Forma):
    def __init__(self, raio: float):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)


class Quadrado(Forma):
    def __init__(self, lado: float):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Triangulo(Forma):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


# Função que aceita qualquer objeto da classe Forma
def imprimir_area(forma: Forma):
    print(f"A área da forma é: {forma.area()}")

# Exemplo de uso
circulo = Circulo(5)  # Raio 5
quadrado = Quadrado(4)  # Lado 4
triangulo = Triangulo(6, 8)  # Base 6, Altura 8

# Usando polimorfismo
imprimir_area(circulo)   # Calcula a área do círculo
imprimir_area(quadrado)  # Calcula a área do quadrado
imprimir_area(triangulo) # Calcula a área do triângulo
