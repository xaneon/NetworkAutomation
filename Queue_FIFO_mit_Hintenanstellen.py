import random
import os
import time

def print_personen(personen):
    os.system("clear")
    for i, person in enumerate(personen):
        print(str(i+1) + ". " + person)

def eliminate_fifo(personen):
    if len(personen) == 0:
        print("Keine Person mehr uebrig.")
    else:
        out = personen.pop(0)
        personen.append(out)
        print_personen(personen)
        print("%s ist fertig." %out)
        time.sleep(2)
        eliminate_fifo(personen)

print("Simulation einer Schlange, FIFO")

anzahl_zufallszahlen = 8
groesste_zahl = 10
zufallszahlen = random.sample(range(1, groesste_zahl), anzahl_zufallszahlen)
personen = ['Person' + str(int(x)) for x in zufallszahlen]
print_personen(personen)
time.sleep(5)
eliminate_fifo(personen)
