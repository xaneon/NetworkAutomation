import threading
import time
import random

class ersterThread(threading.Thread):
    def run(self):
        print("erster Thread schläft")
        time.sleep(random.randint(2, 5))
        print("erster Thread ist fertig")

class zweiterThread(threading.Thread):
    def run(self):
        print("zweiter Thread schläft")
        time.sleep(random.randint(1, 4))
        print("zweiter Thread ist fertig")

t1 = ersterThread()
t2 = zweiterThread()

t1.start()
t2.start()

t1.join()
t2.join()
