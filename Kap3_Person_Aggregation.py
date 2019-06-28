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
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, add, bonus=.10):
        Person.giveRaise(self, add + bonus)

# Zusammensetzung von Objekten zu einer
# Aggregation
class Department:
    def __init__(self, *args):
        self.members = list(args)
        # self.members = args

    def addMember(self, person):
        self.members.append(person)
    # Ruft die Methoden der zusammensetzenden
    # Objekte auf
    def giveRaises(self, add):
            for person in self.members:
                person.giveRaise(add)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev',
                 pay=100000)
    tom = Manager('Tom Jones', 50000)
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()
