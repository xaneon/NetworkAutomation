import abc

class Vogel(abc.ABC):
    @abc.abstractmethod
    def fliegen(self):
        pass

class Singvogel(Vogel):
    def fliegen(self):
        print("Der Singvogel fliegt")

S1 = Singvogel()
S1.fliegen()
V1 = Vogel()  # liefert Fehlermeldung
