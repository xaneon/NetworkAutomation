import threading


class Mythread(threading.Thread):           # subclass Thread object
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count                  # Stateinformation für jeden Thread
        self.mutex = mutex                  # Geteilte objects, keine globals
        threading.Thread.__init__(self)

    def run(self):                          # run liefert den Threadablauf
        for i in range(self.count):
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))


stdoutmutex = threading.Lock()              # Alternativ thread.allocate_lock()
threads = []
for i in range(10):
    thread = Mythread(i, 100, stdoutmutex)
    thread.start()                          # Ruft die run-Methode auf
    threads.append(thread)

for thread in threads:                      # Wartet auf jeden Thread
    thread.join()
print('Main thread exiting.')
