class Car:
    """un'intera macchina"""
    def __init__(self, nome: str, modello: str, colore: str, anno: int):
        self.nome = nome
        self.modello = modello
        self.anno = anno
        self.colore = colore
        self.contachilometri = 0
        
    def descrizione(self):
        """descrive la macchina"""
        print(f"{self.nome} {self.modello} del {self.anno} di colore {self.colore}.")

    def leggi_contachilometri(self):
        """legge i chilometri percorsi"""
        print(f"La macchina ha percorso {self.contachilometri} km.")

    def setta_contachilometri(self, chilometri: int):
        """aggiorna i chilometri percorsi"""
        if chilometri >= self.contachilometri:
            self.contachilometri = chilometri
        else:
            print("Non è possibile diminuire i chilometri percorsi.")

    def incrementa_contachilometri(self, chilometri: int):
        """aggiunge chilometri percorsi"""
        if chilometri >= 0:
            self.contachilometri += chilometri
        else:
            print("Non è possibile diminuire i chilometri percorsi.")
        