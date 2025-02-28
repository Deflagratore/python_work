from pathlib import Path
import json

def get_username(path):
    user_name = input("Come ti chiami? ")
    contenuto = json.dumps(user_name)
    path.write_text(contenuto)
    return user_name

def get_stored_username(path):
    if path.exists():
        contenuto = path.read_text()
        user_name = json.loads(contenuto)
        return user_name
    else:
        return None
    
def greet_user():
    path = Path('username.json')
    user_name = get_stored_username(path)
    if user_name:
        doamnda = input(f"Sei tu {user_name}? (s/n) ")
        if doamnda == 's':
            print(f"Benvenuto {user_name}!")
        else:
            user_name = get_username(path)
    else:
        user_name = get_username(path)
        print(f"Ti ricorderò quando tornerai, {user_name}!")

greet_user()