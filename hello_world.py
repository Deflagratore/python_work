from funzioni import make_album

lista_album: list = []

domanda: str = input("Vuoi inserire un album musicale? ").lower()

if domanda == "si":
    active: bool = True
    
    while active:
        """Ciclo con lo scopo di aggiungere l'input dell'utente in un dizionario"""
        input_artista: str = input("Inserisci il nome dell'artista: ")
        input_album: str = input("Inserisci il nome dell'album: ")
        input_tracce: int = input("Inserisci il numero di tracce dell'album: ")
        lista_album.append(make_album(artista = input_artista, album = input_album, tracce = int(input_tracce)))

        print(lista_album)

        domanda2: str = input("Vuoi inserire un altro album? ").lower()
        if domanda2 == "no":
            active = False
        else:
            continue




