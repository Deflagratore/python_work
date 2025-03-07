def get_players(winner, loser) -> dict:
    user_data = {"vincitore":winner,
                 "perdente":loser}
    return user_data

def write_user_data(user_data: dict, users: dict, id: int) -> dict:
    """Questa funzione scrive i dati utente nel dizionario users"""
    users[id] = user_data
    id += 1
    return users
