"""
 Crie um programa, instancie um objeto da classe Carro e teste o seu médodo
"""
from exercicios.ex5 import Carro

if __name__ == '__main__':
    carro: Carro = Carro(marca='Honda', modelo="Civic", portas=4)
    carro.imprimir()