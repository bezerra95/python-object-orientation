from heranca.produto import Produto
from heranca.cliente import Cliente, ClienteVIP

class Pedido:
    """
    Classe Pedido que representa um pedido realizado por um cliente.
    """

    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_produto(self, produto: Produto):
        self.itens.append(produto)

    def calcular_total(self):
        total = sum([produto.preco for produto in self.itens])
        if isinstance(self.cliente, ClienteVIP):
            total *= (1 - self.cliente.desconto)  # Usando a propriedade desconto
        return total

    def resumo_pedido(self):
        print(f"Pedido de {self.cliente.get_info()}")
        for produto in self.itens:
            print(produto.get_info())
        print(f"Total do pedido: R$ {self.calcular_total():.2f}")
