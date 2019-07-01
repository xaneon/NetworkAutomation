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


class Manager(Person):
    # Neudefinition des Konstruktors ...
    def __init__(self, name, pay):
        # ... verwenet den vererbten
        Person.__init__(self, name, 'mgr', pay)

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
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
