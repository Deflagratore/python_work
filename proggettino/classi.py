import random

class Personaggi:
    """è una classe che inizializza il tipo dei personaggi"""
    
    def __init__(self, nome: str, salute: int = 100, attacco_b: int = 10):
        self.salute = salute
        self.nome = nome
        self.attacco_b = attacco_b

    def show_s(self):
        print(f"\nA {self.nome} rimane {self.salute} punti salute.\n")

    def show_n(self):
        print(f"{self.nome}")

    def reduce_s(self, damage: int):
        """Permette al personaggio di prendere danno"""
        self.damage = damage
        self.salute -= self.damage
        return self.salute

    def attack(self):
        self.damage = random.randint(1, 10)
        return self.damage


class Hero(Personaggi):
    """è un personaggio buono"""

    def __init__(self, nome, salute = 100, attacco_b = 10):
        super().__init__(nome, salute, attacco_b)

class Villain(Personaggi):
    """è un personaggio cattivo"""

    def __init__(self, nome, salute = 100, attacco_b = 10):
        super().__init__(nome, salute, attacco_b)

    def show_s(self):
        print(f"L'avversario ha {self.salute} punti salute\n")  


class Weapons:
    """Sono delle armi equipaggiabili""" 

    def __init__(self, damage: int, speed: int):
        self.damage = damage
        self.speed = speed

    
class Spada(Weapons):
    """è una spada """

    def __init__(self, damage, speed):
        super().__init__(damage, speed)

    def inflick_damage(self):
        self.damage = random.randint(5, 25)
        return self.damage
    
    def c_speed(self):
        self.speed = random.randint(1, 5)
        return self.speed
    

class Arco(Weapons):
    """è un arco"""

    def __init__(self, damage, speed):
        super().__init__(damage, speed)

    def inflick_damage(self):
        self.damage = random.randint(0, 30)
        return self.damage
    
    def c_speed(self):
        self.speed = random.randint(1, 5)
        return self.speed
    
def scegli_arma():
    """{1:"spada", 2:"arco", 3:"pugni"}"""
    numero = random.randint(1, 3)
    if numero == 1:
        arma = "spada"
    elif numero == 2:
        arma = "arco"
    elif numero == 3:
        arma = "pugni"
    return arma
    