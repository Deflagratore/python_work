def magliette(tessuto, taglia, colore):
    """Funzione per la creazione di magliette"""
    print(f"La maglietta è di tessuto {tessuto}, di taglia {taglia} e di colore {colore}")

def city_country(città, stato):
    """funzione che prende una città in uno stato"""
    frase = f"{città}, {stato}"
    return print(frase.title())

def make_album(artista, album, tracce = None):
    """Funzione che crea un dizionario di album musicali"""
    albums = {"Artista": artista, "Album": album}
    if tracce:
        albums["Tracce"] = tracce
    return albums

def make_album2(**albums):
    """Funzione che crea un dizionario di album musicali"""
    return albums

def make_album3(*albums):
    """Funzione che crea una tupla"""
    return albums


