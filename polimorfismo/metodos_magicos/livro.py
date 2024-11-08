
"""
Explicação de cada método mágico:
__init__: Inicializa os atributos do objeto.
__str__: Retorna uma string amigável ao usar print().
__repr__: Retorna uma string detalhada para depuração.
__len__: Retorna o comprimento de um atributo (número de páginas).
__eq__, __ne__: Compara dois objetos para igualdade e desigualdade.
__lt__, __le__, __gt__, __ge__: Compara dois objetos com base no número de páginas.
__add__, __sub__, __mul__: Soma, subtrai e multiplica o número de páginas.
__del__: Executado quando o objeto é destruído.
__call__: Permite "chamar" o objeto como uma função.
__contains__: Verifica se um termo está presente em um atributo (título).
__getitem__, __setitem__, __delitem__: Permitem acessar, modificar e deletar partes do atributo.
Esses métodos tornam os objetos mais integrados com o comportamento padrão das funções e operadores do Python.


No exemplo da classe Livro, o polimorfismo ocorre quando os mesmos operadores ou funções
podem ser usados de maneiras diferentes, dependendo do contexto.
Em Python, isso é implementado com métodos mágicos, como os operadores aritméticos
 e comparativos que personalizamos para o objeto Livro.

Aqui estão os principais pontos de polimorfismo neste exemplo:

Polimorfismo de operadores: Métodos como __add__, __sub__, __mul__, __eq__, __lt__
permitem que você use operadores matemáticos (+, -, *) e comparativos (==, <)
em objetos da classe Livro. Ao invés de operar com números ou strings,
esses operadores agora trabalham com os atributos dos objetos Livro,
como o número de páginas.
"""

class Livro:
    """
    Classe Livro com métodos mágicos para ilustrar seu uso e comportamento.
    """

    def __init__(self, titulo: str, autor: str, paginas: int):
        """
        Método mágico __init__: Inicializa os atributos de um livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        """
        Método mágico __str__: Retorna uma representação amigável do livro (usado com print()).
        """
        return f"'{self.titulo}' por {self.autor}, {self.paginas} páginas"

    def __repr__(self):
        """
        Método mágico __repr__: Retorna uma representação detalhada (usado no terminal e debugging).
        """
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas})"

    def __len__(self):
        """
        Método mágico __len__: Retorna o número de páginas (usado com len()).
        """
        return self.paginas

    def __eq__(self, outro):
        """
        Método mágico __eq__: Compara se dois livros têm o mesmo título e autor.
        """
        if isinstance(outro, Livro):
            return self.titulo == outro.titulo and self.autor == outro.autor
        return False

    def __ne__(self, outro):
        """
        Método mágico __ne__: Retorna True se os livros forem diferentes.
        """
        return not self.__eq__(outro)

    def __lt__(self, outro):
        """
        Método mágico __lt__: Verifica se este livro tem menos páginas que outro.
        """
        return self.paginas < outro.paginas

    def __le__(self, outro):
        """
        Método mágico __le__: Verifica se este livro tem menos ou o mesmo número de páginas que outro.
        """
        return self.paginas <= outro.paginas

    def __gt__(self, outro):
        """
        Método mágico __gt__: Verifica se este livro tem mais páginas que outro.
        """
        return self.paginas > outro.paginas

    def __ge__(self, outro):
        """
        Método mágico __ge__: Verifica se este livro tem mais ou o mesmo número de páginas que outro.
        """
        return self.paginas >= outro.paginas

    def __add__(self, outro):
        """
        Método mágico __add__: Soma o número de páginas de dois livros.
        """
        if isinstance(outro, Livro):
            return self.paginas + outro.paginas
        return NotImplemented

    def __sub__(self, outro):
        """
        Método mágico __sub__: Subtrai o número de páginas de dois livros.
        """
        if isinstance(outro, Livro):
            return self.paginas - outro.paginas
        return NotImplemented

    def __mul__(self, n):
        """
        Método mágico __mul__: Multiplica o número de páginas por um número inteiro.
        """
        if isinstance(n, int):
            return self.paginas * n
        return NotImplemented

    def __del__(self):
        """
        Método mágico __del__: Chamado quando o objeto é destruído (usado para limpeza de recursos).
        """
        print(f"O livro '{self.titulo}' foi removido da memória.")

    def __call__(self):
        """
        Método mágico __call__: Permite que o objeto seja "chamado" como uma função.
        """
        return f"Este livro é '{self.titulo}', escrito por {self.autor}, com {self.paginas} páginas."

    def __contains__(self, palavra):
        """
        Método mágico __contains__: Verifica se uma palavra está presente no título do livro.
        """
        return palavra in self.titulo

    def __getitem__(self, index):
        """
        Método mágico __getitem__: Permite acessar caracteres do título como uma lista (usado com colchetes).
        """
        return self.titulo[index]

    def __setitem__(self, index, valor):
        """
        Método mágico __setitem__: Permite alterar caracteres no título usando colchetes.
        """
        titulo_lista = list(self.titulo)
        titulo_lista[index] = valor
        self.titulo = ''.join(titulo_lista)

    def __delitem__(self, index):
        """
        Método mágico __delitem__: Permite deletar caracteres do título usando colchetes.
        """
        titulo_lista = list(self.titulo)
        del titulo_lista[index]
        self.titulo = ''.join(titulo_lista)


# Exemplos de uso dos métodos mágicos

# Criando dois livros
livro1 = Livro("Python Avançado", "João Silva", 400)
livro2 = Livro("Introdução ao Python", "Maria Lima", 300)

# __str__ e __repr__
print(str(livro1))  # 'Python Avançado' por João Silva, 400 páginas
print(repr(livro2))  # Livro(titulo='Introdução ao Python', autor='Maria Lima', paginas=300)

# __len__
print(len(livro1))  # 400

# __eq__, __ne__, __lt__, __le__, __gt__, __ge__
print(livro1 == livro2)  # False
print(livro1 != livro2)  # True
print(livro1 > livro2)  # True
print(livro1 >= livro2)  # True

# __add__, __sub__, __mul__
print(livro1 + livro2)  # Soma das páginas: 700
print(livro1 - livro2)  # Diferença das páginas: 100
print(livro1 * 2)  # Multiplicação das páginas: 800

# __contains__
print("Python" in livro1)  # True (a palavra 'Python' está no título)

# __getitem__, __setitem__, __delitem__
print(livro1[0])  # P (primeiro caractere do título)
livro1[0] = 'C'  # Mudando o título
print(livro1.titulo)  # Cython Avançado
del livro1[0]  # Deletando o primeiro caractere
print(livro1.titulo)  # ython Avançado

# __call__
print(livro1())  # Chama o objeto como função

# __del__ (chamado automaticamente quando o objeto é destruído)
del livro1
