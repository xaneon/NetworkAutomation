class Ente:
    def __init__(self, name):
        self.name = name
        self.pub = "Ich bin öffentlich"
        self._prot = "Ich bin protected"
        self.__priv = "Ich bin private"


meineEnte = Ente("Ente Helga")
print(meineEnte.name)
print(meineEnte.pub)
print(meineEnte._prot)
# print(meineEnte.__priv)  # funktioniert nicht
