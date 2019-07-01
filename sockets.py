import socket
# help(socket)
HOST = "178.77.107.36"
PORT = 80
ADDR = (HOST, PORT)

mysocket = socket.socket(socket.AF_INET, 
                         socket.SOCK_STREAM)

mysocket.connect(ADDR)
print(mysocket, type(mysocket))
