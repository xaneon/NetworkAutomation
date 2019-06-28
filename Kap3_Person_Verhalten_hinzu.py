class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    # Methoden um das Verhalten festzulegen
    # self wird immer als Subjekt impliziert
    # Ändereungen werden nur hier vorgenommen
    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, add):
        self.pay = int(self.pay * (1 + add))


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev',
                 pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    # Benutzung der neuen Methoden
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
