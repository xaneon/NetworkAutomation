class Ente(object):
    def fliegen(self):
        print("Die Ente fliegt")
class Flugzeug(object):
    def fliegen(self):
        print("Das Flugzeug fliegt")
class Fisch(object):
    def schwimmen(self):
        print("Der Fisch schwimmt")

def kann_objekt_fliegen(instanzvariable):
    instanzvariable.fliegen()

E1 = Ente()
F1 = Flugzeug()
Fi1 = Fisch()

kann_objekt_fliegen(E1)
kann_objekt_fliegen(F1)
kann_objekt_fliegen(Fi1)
