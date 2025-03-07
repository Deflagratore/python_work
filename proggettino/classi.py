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

    def check_death(self, death=False):
        lista = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10,
                 -11, -12, -13, -14, -15, -16, -17, -18, -19,
                 -20, -21, -22, -23, -24, -25, -26, -27, -28,
                 -29, -30, -31, -32, -33, -34, -35, -36, -37]
        if self.salute in lista:
            death = True
        return death


class Hero(Personaggi):
    """è un personaggio buono"""

    def __init__(self, nome, salute = 100, attacco_b = 10):
        super().__init__(nome, salute, attacco_b)

    def attack(self):
        try:
            domanda = input("\nChe arma vuoi equipaggiare: spada, arco o pugni? ").lower()
            if domanda == "spada":
                self.damage = random.randint(5, 25)
                return self.damage
            elif domanda == "arco":
                self.damage = random.randint(0, 30)
                return self.damage
            elif domanda == "pugni":
                self.damage = random.randint(1, 15)
                return self.damage
            else:
                self.damage = 1
                return self.damage
        except ValueError as e:
            print("Inserire uno dei valori forniti")
        
        return self.damage
            


class Villain(Personaggi):
    """è un personaggio cattivo"""

    def __init__(self, nome, salute = 100, attacco_b = 10):
        super().__init__(nome, salute, attacco_b)

    def show_s(self):
        print(f"L'avversario ha {self.salute} punti salute\n")  

    def attack(self):
        domanda = random.randint(1, 3)
        if domanda == 1:
            self.damage = random.randint(5, 25)
            return self.damage
        elif domanda == 2:
            self.damage = random.randint(0, 30)
            return self.damage
        elif domanda == 3:
            self.damage = random.randint(1, 15)
            return self.damage
        return self.damage
        


    



    
    