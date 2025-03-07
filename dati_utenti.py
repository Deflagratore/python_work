from pathlib import Path
import json
import funzioniperdu as fp

path = Path("dati_utenti.json")
active: bool = True

users: dict = {}

id: int = 1

print("Benvenuto nel programma di inserimento dati utente\n")

while active:
    try:
        name: str = input("Inserisci il tuo nome: ")
        if name.isdigit():
            raise ValueError("Il nome deve essere una stringa")
    except ValueError as e:
        print(e)
        continue
    
    try:    
        surname: str = input("Inserisci il tuo cognome: ")
        if surname.isdigit():
            raise ValueError("Il cognome deve essere una stringa")
    except ValueError as e:
        print(e)
        continue

    try:   
        age = int(input("Inserisci la tua età: "))
        if age < 0:
            raise ValueError("L'età deve essere un numero positivo")
        if age == str:
            raise ValueError("L'età deve essere un numero")
    except ValueError as e:
        print(e)
        continue

    user_data = fp.get_user_data(name, surname, age)
    users = fp.write_user_data(user_data=user_data, users=users, id=id)
    id += 1

    domanda = input("Vuoi inserire un altro utente? (s/n) ")
    if domanda == "n":
        try:
            s_users = json.dumps(users)
            path.write_text(s_users)
        except FileNotFoundError:
            print("Il file non è stato trovato")
        
        print(users)
        active = False
    else:
        continue


