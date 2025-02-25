from funzioni import make_album

lista_album = []

domanda = input("Vuoi inserire un album musicale? ").lower()

if domanda == "si":
    active = True
    
    while active:
        input_artista = input("Inserisci il nome dell'artista: ")
        input_album = input("Inserisci il nome dell'album: ")
        input_tracce = input("Inserisci il numero di tracce dell'album: ")
        lista_album.append(make_album(artista = input_artista, album = input_album, tracce = int(input_tracce)))

        print(lista_album)

        domanda2 = input("Vuoi inserire un altro album? ").lower()
        if domanda2 == "no":
            active = False
        else:
            continue




