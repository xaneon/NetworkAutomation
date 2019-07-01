import socket
import ssl
import sys

HOSTNAME = 'www.python.org'
PORT = 443
BUFFSIZE = 4096
ADDR = (HOSTNAME, PORT)
CONTEXT = ssl.create_default_context()

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    tcp_sock.connect(ADDR)
    print("Socket verbunden.")
except socket.error as err:
    print("Verbindungsversuch fehlgeschlagen.")
    tcp_sock.close()
    sys.exit()

REQ = "GET / HTTP/1.1\nHost: {}\n\n".format(HOSTNAME).encode("utf-8")
tcp_sock.send(REQ)
result = tcp_sock.recv(BUFFSIZE).decode("utf-8")
print(result)
while (len(result) > 0):
    result = tcp_sock.recv(BUFFSIZE).decode("utf-8")
    print(result)
