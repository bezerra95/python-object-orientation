"""
Abstração: As classes abstraem o conceito de produtos, clientes e pedidos do mundo real.

Encapsulamento: Os atributos nome, preco, cpf, e itens estão encapsulados dentro das classes,
protegendo os dados e controlando o acesso através de métodos.

Objetos: As instâncias cliente1, produto1, produto2 e pedido1
são objetos das respectivas classes.

Herança: A classe ProdutoEletronico herda da classe Produto.
Isso significa que ProdutoEletronico pode reutilizar todos os atributos
e métodos de Produto e adicionar ou modificar comportamento, como o atributo garantia.
"""

class Produto:
    """
    Classe que representa um produto, com propriedades para nome e preço.
    """
    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco

    # Propriedade para acessar o nome do produto
    @property
    def nome(self):
        return self._nome

    # Propriedade setter para modificar o nome do produto
    @nome.setter
    def nome(self, novo_nome: str):
        if len(novo_nome) > 0:
            self._nome = novo_nome
        else:
            raise ValueError("O nome do produto não pode ser vazio.")

    # Propriedade para acessar o preço do produto
    @property
    def preco(self):
        return self._preco

    # Propriedade setter para modificar o preço do produto
    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco > 0:
            self._preco = novo_preco
        else:
            raise ValueError("O preço deve ser maior que zero.")

    def get_info(self):
        return f"Produto: {self.nome}, Preço: R$ {self.preco:.2f}"



class ProdutoEletronico(Produto):
    """
    Classe que representa um produto eletrônico com garantia adicional.
    """
    def __init__(self, nome: str, preco: float, garantia: int):
        # Chama o construtor da superclasse (Produto) para inicializar nome e preco
        super().__init__(nome, preco)
        self._garantia = garantia

    @property
    def garantia(self):
        return self._garantia

    @garantia.setter
    def garantia(self, meses: int):
        if meses >= 0:
            self._garantia = meses
        else:
            raise ValueError("A garantia deve ser um valor positivo.")

    def get_info(self):
        return f"{super().get_info()}, Garantia: {self.garantia} meses"
