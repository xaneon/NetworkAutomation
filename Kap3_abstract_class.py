from abc import ABC, abstractmethod

class abstrakteKlasse(ABC):
    def __init__(self, wert):
        self.wert = wert
        super().__init__()

    @abstractmethod
    def methode(self):
        print("Implementation einer Methode")

class unterKlasse(abstrakteKlasse):
    def methode(self):
        super().methode()
        print(self.wert)

U = unterKlasse(42)
U.methode()

A = abstrakteKlasse(42)
