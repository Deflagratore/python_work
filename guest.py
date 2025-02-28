from pathlib import Path

path = Path("lista_ospiti.txt")

nomi = ""

active = True

while active:
    name = input("Ciao, come ti chiami? ")
    
    nomi += f"{name} e stato aggiunto alla lista\n"

    print(f"Benvenuto {name}! Sei stato aggiunto alla lista degli ospiti!")

    if input("Vuoi aggiungere un altro ospite? (s/n): ") == "n":
        path.write_text(nomi)
        print("Lista degli ospiti salvata con successo!")
        active = False
    else:
        continue
