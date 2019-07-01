import numpy as np
class WertZuKleinFehler(ValueError):
    pass

class WertZuGrossFehler(ValueError):
    pass

class ZahlRaten:
    def __init__(self, zahl=42):
        self.zahl = zahl
    def raten(self, text="Raten Sie die Zahl"):
        guess = int(input(text + ": "))
        try:
            if(guess < self.zahl):
                raise WertZuKleinFehler()
            elif(guess > self.zahl):
                raise WertZuGrossFehler()
            else:
                print("Korrekte Zahl geraten!")
        except WertZuKleinFehler:
            print("Geratene Zahl zu klein.\n")
            self.raten("Neuer Versuch")
        except WertZuGrossFehler:
            print("Geratene Zahl zu gross.\n")
            self.raten("Neuer Versuch")

if __name__ == "__main__":
    zahl = ZahlRaten(np.random.randint(0, 99))
    zahl.raten()
