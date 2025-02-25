def magliette(tessuto: str, taglia: str, colore: str) -> str:
    """Funzione per la creazione di magliette"""
    print(f"La maglietta è di tessuto {tessuto}, di taglia {taglia} e di colore {colore}")

def city_country(città: str, stato: str) -> str:
    """funzione che prende una città in uno stato"""
    frase = f"{città}, {stato}"
    return print(frase.title())

def make_album(artista: str, album: str, tracce: int = None) -> dict:
    """Funzione che crea un dizionario di album musicali"""
    albums: dict = {"Artista": artista, "Album": album}
    if tracce:
        albums["Tracce"] = tracce
    return albums

def make_album2(**albums: dict) -> dict:
    """Funzione che crea un dizionario di album musicali"""
    return albums

def make_album3(*albums: tuple) -> tuple:
    """Funzione che crea una tupla"""
    return albums


