import classi as cs

nickname = input("Inserisci il nome del tuo personaggio: ")

active = True

print("La battaglia ha inizio!\n")
hero = cs.Hero(nickname)
enemy = cs.Villain("Avversario")

domanda1 = True

lista: list[int] = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

while active:
    hero.show_s()
    enemy.show_s()
    
    while domanda1:
        domanda = input("\nVuoi attacare? ")
        hero.reduce_s(damage=enemy.attack())
        enemy.reduce_s(damage=hero.attack())
        hero.show_s()
        enemy.show_s()
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
