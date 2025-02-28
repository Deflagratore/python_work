from pathlib import Path

active: bool = True
lista_somme = ""
path = Path("lista_operazioni.txt")

print("Ciao, inserisci due numeri per fare una somma")

while active:
    try:
        num1 = int(input("Inserisci il primo numero: "))
        num2 = int(input("Inserisci il secondo numero: "))
    except ValueError:
        print("Devi inserire un numero")
    else:
        somma = num1 + num2
        lista_somme += f"{num1} + {num2} = {somma}\n"
        print(f"La somma tra {num1} e {num2} è {num1 + num2}")
        
        if input("Vuoi fare un'altra somma? (s/n): ") == "n":
            path.write_text(lista_somme)
            active = False
        else:
            continue