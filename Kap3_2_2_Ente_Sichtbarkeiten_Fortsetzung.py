class Ente:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def gibLaut(self):
        print("quak", self.__name)

    def __private(self):
        pass


meineEnte = Ente("Ente Helga")
# print(meineEnte.__name)  # Fehler
print(meineEnte.getName())
meineEnte.setName("Ente Helmut")
print(meineEnte.getName())
meineEnte.gibLaut()
# meineEnte.__private()  # Fehler
