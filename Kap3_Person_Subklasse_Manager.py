class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, add):
        self.pay = int(self.pay * (1 + add))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name,
                                     self.pay)


# Neue Klasse Manager die Person erweitert
class Manager(Person):
    def giveRaise(self, add, bonus=.10):
        Person.giveRaise(self, add + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev',
                 pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    # Erzeuge einen Manager: __init__
    tom = Manager('Tom Jones', 'mgr', 50000)
    # Verwendung der Angebpassten Methode
    tom.giveRaise(.10)
    # Verwendung der vererbten Methoden
    print(tom.lastName())
    print(tom)
