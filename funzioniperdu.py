def get_user_data(name: str, surname: str, age: int) -> dict:
    """Questa funzione prende i dati utente e li restituisce come dizionario"""
    user_data = {
        "name": name,
        "surname": surname,
        "age": age
    }
    return user_data

def write_user_data(user_data: dict, users: dict, id: int) -> dict:
    """Questa funzione scrive i dati utente nel dizionario users"""
    users[id] = user_data
    id += 1
    return users