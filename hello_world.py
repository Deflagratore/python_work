d1 = {'a': "python", 'b': "java", 'c': "c++", 'd': "c#", 'e': "ruby", 'f': "perl"}

for key, value in d1.items():
    print(f"{key} => {value}")

d1['g'] = "php"
d1['h'] = "javascript"
d1['i'] = "html"
d1['j'] = "css"
d1['k'] = "sql"

for key, value in d1.items():
    print(f"{key} => {value}")

d2 = {"egitto": "nilo", "italia": "tiber", "francia": "senna",}

for key, value in d2.items():
    print(f"in {key} scorre il {value}")

for value in d2.values():
    print(value)

for key in d2.keys():
    print(key)
persone_cattive = ["marco","giovanni","luca"] 

persone_invitate = {"marco": "no", "giovanni": "no", "luca": "no",
                     "mario": "si", "giuseppe": "si", "francesco": "si",
                     "antonio": "si", "luigi": "si", "giovanna": "si",}

for name in persone_invitate.keys():
    if name in persone_cattive:
        print(f"Rispondi al sondaggio {name}")
    else:
        print(f"Ciao {name}, grazie per aver risposto")

#.keys() restituisce una lista di chiavi
#.values() restituisce una lista di valori


d3 = {"nome": "marco", "cognome": "rossi", "eta": 25, "professione": "programmatore",
 "linguaggi": ["python", "java", "c++", "c#", "ruby"],}

d4 = {"nome": "giovanni", "cognome": "verdi", "eta": 30, "professione": "analista",}

d5 = {"nome": "luca", "cognome": "bianchi", "eta": 35, "professione": "ingegnere",
"specializzazione" : {"elettronica": "molecolare", "informatica" : "quantistica",
 "meccanica" : "avanzata"},}

possibili_impiegati = [d3, d4, d5]

for impiegato in possibili_impiegati:
    print(f"\nNome: {impiegato['nome']}")
    print(f"Cognome: {impiegato['cognome']}")
    print(f"Età: {impiegato['eta']}")
    print(f"Professione: {impiegato['professione']}")
    if "linguaggi" in impiegato:
        print(f"Linguaggi conosciuti: {impiegato['linguaggi']}")
    if "specializzazione" in impiegato:
        print(f"Specializzazione: {impiegato['specializzazione']}")

print("\nFine del programma")