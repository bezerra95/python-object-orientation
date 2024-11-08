"""
ClienteVIP: Herda de Cliente e adiciona o atributo desconto.
Se o cliente for VIP, o desconto é aplicado no total do pedido.
ProdutoEletronico: Herda de Produto e adiciona o atributo garantia.
Pedido: Verifica se o cliente é do tipo ClienteVIP e aplica o desconto ao calcular o total.
Encapsulamento: As informações são protegidas, e o acesso a detalhes como o nome e o preço
é feito através de métodos como get_info.
"""
# main.py
from heranca.produto import Produto, ProdutoEletronico
from heranca.cliente import ClienteVIP
from classes.pedido import Pedido

# Criando um cliente VIP
cliente_vip = ClienteVIP("Maria Silva", "123.456.789-00", 0.10)  # 10% de desconto

# Criando alguns produtos
produto1 = Produto("Notebook", 3500.00)
produto2 = ProdutoEletronico("Smartphone", 2000.00, 24)  # Produto eletrônico com 24 meses de garantia

# Criando um pedido para o cliente VIP
pedido1 = Pedido(cliente_vip)

# Adicionando produtos ao pedido
pedido1.adicionar_produto(produto1)
pedido1.adicionar_produto(produto2)

# Exibindo o resumo do pedido
pedido1.resumo_pedido()
