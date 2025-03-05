import classi as cs
from classi import scegli_arma

nickname = input("Inserisci il nome del tuo personaggio: ")

hero = cs.Hero(nickname)
enemy = cs.Villain("Avversario")

active = True

arco = cs.Arco(2, 3)

spada = cs.Spada(1, 3)

domanda2 = input("Quale arma scegli: la spada, l'arco o i tuoi pugni? ").lower()

if domanda2 == "spada":
    damage = spada.inflick_damage()
elif domanda2 == "arco":
    damage = arco.inflick_damage()
else:
    damage = hero.attack()

arma = scegli_arma()

if arma == "spada":
    damage2 = spada.inflick_damage()
elif arma == "arco":
    damage2 = arco.inflick_damage()
elif arma == "pugni":
    damage2 = enemy.attack()

print("\nLa battaglia ha inizio!\n")

domanda1 = True

tick = True

lista: list[int] = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

while active:
    hero.show_s()
    enemy.show_s()
    
    while domanda1:
        if hero.salute or enemy.salute not in lista:
            domanda = input("\nVuoi attacare? ")
            hero.reduce_s(damage=damage2)
            enemy.reduce_s(damage=damage)
            hero.show_s()
            enemy.show_s()
        else:
            print("\nIl combattimento è finito!\n")
        
        if domanda == "no":
            if hero.salute > enemy.salute:
                winner = hero.nome
            if enemy.salute > hero.salute:
                winner = enemy.nome
            domanda1 = False
            break
        
        for number in range(0, -10):
            if hero.salute or enemy.salute == number:
                if hero.salute > enemy.salute:
                    winner = hero.nome
                    domanda1 = False
                    break
                if enemy.salute > hero.salute:
                    winner = enemy.nome
                    domanda1 = False 
                    break
    
    print("\nLa partita è finita!\n")
    
    if domanda1 == False:
        break

print(f"Il vincitore è {winner}!")
