class Ente:

    zaehler = 0

    def __init__(self, name):
        self.__name = name
        Ente.zaehler += 1
        print("Ente Nummer " +
              str(Ente.zaehler) + " lebt!")

    def __del__(self):
        Ente.zaehler -= 1
        print(self.__name, " ist nicht mehr!")

    @staticmethod
    def gibAnzahlEnten():
        return Ente.zaehler


a = Ente("QuitscheEnte")
b = Ente("EnteB")
c = Ente("EnteC")
print(a.zaehler)
print(Ente.zaehler)
del b
print(a.zaehler)
print(Ente.gibAnzahlEnten())
print(a.gibAnzahlEnten())
