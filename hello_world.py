domanda1 = "Come ti chiami? "
domanda2 = "Che luogo mi consigli di visitare? "

lp = {}

Active = True

while Active:
    nome = input(domanda1)
    if nome.isdigit():
        print("Inserire un nome valido")
        continue

    luogo = input(domanda2)
    if luogo.isdigit():
        print("Inserire un luogo valido")
        continue

    lp[nome] = luogo

    print("Vuoi continuare?")
    risposta = input("Si/No: ").lower()
    if risposta == "no":
        Active = False
        print(lp)
    else:
        continue



