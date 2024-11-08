"""
3. Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de
forma que:
 a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
 b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
 c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também
permitir que seja informado um número de canal para efetuar a troca
"""


class Televisao:
    def __init__(self):
        self._status = False  # A TV começa desligada
        self._volume = 10     # Volume inicial
        self._canal = 1       # Canal inicial

    # Getter e Setter para status
    @property
    def status(self):
        return "Ligada" if self._status else "Desligada"

    def ligar(self):
        if not self._status:
            self._status = True
            print("A TV está agora ligada.")
        else:
            print("A TV já está ligada.")

    def desligar(self):
        if self._status:
            self._status = False
            print("A TV está agora desligada.")
        else:
            print("A TV já está desligada.")

    # Getter e Setter para volume
    @property
    def volume(self):
        return self._volume

    def aumentar_volume(self):
        if self._status:
            if self._volume < 100:
                self._volume += 1
                print(f"Volume aumentado para {self._volume}")
            else:
                print("O volume já está no máximo.")
        else:
            print("A TV está desligada. Não é possível alterar o volume.")

    def diminuir_volume(self):
        if self._status:
            if self._volume > 0:
                self._volume -= 1
                print(f"Volume diminuído para {self._volume}")
            else:
                print("O volume já está no mínimo.")
        else:
            print("A TV está desligada. Não é possível alterar o volume.")

    # Getter e Setter para canal
    @property
    def canal(self):
        return self._canal

    def aumentar_canal(self):
        if self._status:
            self._canal += 1
            print(f"Canal aumentado para {self._canal}")
        else:
            print("A TV está desligada. Não é possível alterar o canal.")

    def diminuir_canal(self):
        if self._status:
            if self._canal > 1:
                self._canal -= 1
                print(f"Canal diminuído para {self._canal}")
            else:
                print("O canal já está no mínimo.")
        else:
            print("A TV está desligada. Não é possível alterar o canal.")

    def trocar_canal(self, novo_canal: int):
        if self._status:
            if novo_canal > 0:
                self._canal = novo_canal
                print(f"Canal alterado para {self._canal}")
            else:
                print("Número de canal inválido.")
        else:
            print("A TV está desligada. Não é possível alterar o canal.")
 

class ControleRemoto:
    def __init__(self, televisao: Televisao):
        self.televisao = televisao

    # Métodos de controle via controle remoto
    def ligar(self):
        self.televisao.ligar()

    def desligar(self):
        self.televisao.desligar()

    def aumentar_volume(self):
        self.televisao.aumentar_volume()

    def diminuir_volume(self):
        self.televisao.diminuir_volume()

    def aumentar_canal(self):
        self.televisao.aumentar_canal()

    def diminuir_canal(self):
        self.televisao.diminuir_canal()

    def trocar_canal(self, novo_canal: int):
        self.televisao.trocar_canal(novo_canal)


# Testando as classes
tv = Televisao()
controle = ControleRemoto(tv)

# Ligando a TV via controle
controle.ligar()

# Aumentando o volume e canal via controle
controle.aumentar_volume()
controle.aumentar_canal()

# Trocando o canal diretamente para 5
controle.trocar_canal(5)

# Diminuindo o volume e canal
controle.diminuir_volume()
controle.diminuir_canal()

# Desligando a TV via controle
controle.desligar()
