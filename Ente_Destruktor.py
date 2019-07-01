class Ente:

    def __init__(self, name):
        self.__name = name
        print("Ente lebt!")

    def __del__(self):
        print("Ente lebt nicht mehr!")


e = Ente("QuitscheEnte")  # Ente lebt!

del e  # Ente lebt nicht mehr
