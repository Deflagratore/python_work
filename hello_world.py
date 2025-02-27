import car # importa la classe Car dal modulo car

class Restaurant: # è una classe
    """una classe che crea un ristorante"""
    def __init__(self, name: str, cousine: str):
        self.name = name
        self.cousine = cousine
        self.number_served: int = 0 # attributo della classe Restaurant

    def describe_restaurant(self): # è un metodo della classe Restaurant
        """descrive nome e tipo di cibo del ristorante"""
        print(f"{self.name} serve {self.cousine}.")

    def open_restaurant(self): 
        """scive se il ristorante è aperto"""
        print(f"{self.name} è aperto.")

    def set_number_served(self, number: int): 
        """imposta il numero di clienti serviti"""
        self.number_served = number #attributo salvato nella varabile number

    def read_number_served(self): 
        """legge il numero di clienti serviti"""
        print(f"Abbiamo servito {self.number_served} clienti.")

    def increment_number_served(self, increment: int): 
        """incrementa il numero di clienti serviti"""
        self.number_served += increment

class Icecreamstand(Restaurant): # è una sottoclasse di Restaurant
    """una classe che crea un chiosco di gelati"""
    def __init__(self, name: str, cousine: str, flavors: list):
        super().__init__(name, cousine) # chiama il metodo __init__ della classe padre
        self.flavors = flavors

    def show_flavors(self): 
        """mostra i gusti disponibili"""
        print("I gusti disponibili sono:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor: str): 
        """aggiunge un gusto"""
        self.flavors.append(flavor)

my_restaurant = Restaurant("pizzalandia", "pizza") # è un'istanza della classe Restaurant
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(10)
my_restaurant.read_number_served()
my_restaurant.increment_number_served(5)
my_restaurant.read_number_served()

zeno_restaurant = Restaurant("zenogay", "kebab")
zeno_restaurant.describe_restaurant()

rui_restaurant = Icecreamstand("fantastickrui", "gelato", 
["cioccolato", "vaniglia", "fragola"])

rui_restaurant.describe_restaurant() # ereditato dalla classe Restaurant
rui_restaurant.show_flavors()
rui_restaurant.add_flavor("pistacchio")
rui_restaurant.show_flavors()

Fiat = car.Car("Fiat", "Panda", "rossa", 2000) # è un'istanza della classe Car
Fiat.descrizione()
Fiat.leggi_contachilometri()
Fiat.setta_contachilometri(100)
Fiat.leggi_contachilometri()
Fiat.incrementa_contachilometri(50)
Fiat.leggi_contachilometri()