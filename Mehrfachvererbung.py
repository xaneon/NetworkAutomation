class KlasseA:
    def methode(self):
        print("Methode in KlasseA")

class KlasseB(KlasseA):
    def methode(self):
        print("Methode in KlasseB")

class KlasseC(KlasseA):
    def methode(self):
        print("Methode in KlasseC")

class KlasseD(KlasseC, KlasseB):
    pass

kd = KlasseD()
kd.methode()
