import abc

class Fluegel(object):
    def __init__(self, anzahl=2):
        self.anzahl = anzahl
        self.fluegelInBewegung = False
    def schlagen(self):
        self.fluegelInBewegung = True

class Schnabel(object):
    def __init__(self, farbe="gelb"):
        self.schnabelfarbe = farbe
        self.schnabeloffen = False
    def oeffnen(self):
        self.schnabeloffen = True
    def schliessen(self):
        self.schnabeloffen = False

class InterfaceVogel(Fluegel, Schnabel, abc.ABC):
    @abc.abstractmethod
    def fliegen(self):
        pass

class Singvogel(InterfaceVogel):
    def fliegen(self):
        super().oeffnen()
        super().schlagen()
        fbew, soff = "", ""
        if (self.fluegelInBewegung):
            fbew = "Fluegel in Bewegung"
        if(self.schnabeloffen):
            soff = "Schnabel offen"
        return "Der Singvogel fliegt, " + fbew + ", " + soff

class Spatz(InterfaceVogel):
    def fliegen(self):
        super().schlagen()
        super().schliessen()
        fbew, soff = "", ""
        if (self.fluegelInBewegung):
            fbew = "Fluegel in Bewegung"
        if(self.schnabeloffen):
            soff = "Schnabel offen"
        else:
            soff = "Schnabel geschlossen"
        return "Der Spatz fliegt, " + fbew + ", " + soff

S1 = Singvogel()
print(S1.fliegen())

S2 = Spatz()
print(S2.fliegen())

V1 = InterfaceVogel()
