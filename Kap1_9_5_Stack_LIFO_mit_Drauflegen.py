import random
import os
import time

def print_gegenstande(gegenstande):
    os.system("clear")
    for i, gegenstand in enumerate(gegenstande):
        print(str(len(gegenstande) - i) + ". " + gegenstand)

def eliminate_fifo(gegenstande):
    if len(gegenstande) == 0:
        print("Kein Gegenstand mehr uebrig.")
    else:
        out = gegenstande.pop(0)
        gegenstande.insert(0,out)
        print_gegenstande(gegenstande)
        print("%s herausgenommen." %out)
        time.sleep(2)
        eliminate_fifo(gegenstande)


print("Simulation einer Schlange, FIFO")

anzahl_zufallszahlen = 8
groesste_zahl = 10
zufallszahlen = random.sample(range(1, groesste_zahl), anzahl_zufallszahlen)
gegenstande = ['Gegenstand' + str(int(x)) for x in zufallszahlen]
print_gegenstande(gegenstande)
time.sleep(5)
eliminate_fifo(gegenstande)
