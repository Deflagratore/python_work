class Employ:
    def __init__(self, name: str, surname: str, salary: int):
        self.name = name
        self.surname = surname
        self.salary = salary

    def get_raise(self, raise_amount: int = 5000):
        self.raise_amount = raise_amount
        self.salary += raise_amount
        return self.salary