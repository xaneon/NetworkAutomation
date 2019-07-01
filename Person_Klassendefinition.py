# Definition der Klasse
class Person:
    # Methode zur Initialisierung
    def __init__(self, name, job=None, pay=0):
        # self um die Variable der jeweiligen
        # Instanz zuzuordnen
        self.name = name
        self.job = job
        self.pay = pay

# Ablauf für den Selbsttest
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev',
                 pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
