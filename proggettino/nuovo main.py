import classi as cs
import json
from pathlib import Path
import funzioni_per_dati as pd

path = Path("Liste_vittorie.json")
id: int = 1
users: dict[int,dict] = {}

while True:
    nickname = input("Inserisci il tuo nickname: ") 

    hero = cs.Hero(nickname)
    villain = cs.Villain("Avversario")

    print(f"\nLa battaglia ha inizio, {nickname}!")

    while True:
        hero.show_s()
        villain.show_s()

        death1 = hero.check_death() 
        death2 = villain.check_death()

        if death1 or death2 == True:
            print("\nLa battaglia è finita!")
            if hero.salute >= villain.salute:
                winner = nickname
                loser = "Avversario"
            elif villain.salute >= hero.salute:
                winner = "Avversario"
                loser = nickname
            print(f"\nIl vincitore è {winner}, complimenti!")
            break

        domanda = input("\nVuoi attaccare? ")

        if domanda == "si":
            damage1 = villain.attack()
            damage2 = hero.attack()

            hero.reduce_s(damage=damage1)
            villain.reduce_s(damage=damage2)
            continue
        else:
            print("\nLa battaglia è finita!")
            if hero.salute >= villain.salute:
                winner = nickname
                loser = "Avversario"
            elif villain.salute >= hero.salute:
                winner = "Avversario"
                loser = nickname
            print(f"\nIl vincitore è {winner}, complimenti!")
            break
    
    user_data = pd.get_players(winner=winner, loser=loser)
    dati_vittorie = pd.write_user_data(user_data=user_data, users=users, id=id)
    id += 1
    
    domanda1 = input("Vuoi continuare a giocare? ")

    if domanda1 == "si":
        continue
    else:
        saved_battles = json.dumps(dati_vittorie)
        path.write_text(saved_battles)
        break

print("\nProgramma chiuso")
