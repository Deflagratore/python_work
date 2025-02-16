ingredienti_disponibili = ["pomodoro", "mozzarella", "olio", "sale", "pepe", "salame"]

ingredienti_richiesti = input("Inserisci gli ingredienti che vuoi: ").lower().split(", ")

for ingrediente in ingredienti_richiesti:
    if ingrediente not in ingredienti_disponibili:
        print(f"Mi dispiace, non abbiamo {ingrediente}")
        break
    else:
        print("Ingredienti aggiunti alla pizza")

print("Pizza pronta!")