import socket
import ssl
import sys

HOSTNAME = 'github.com'
PORT = 80
BUFFSIZE = 4096
ADDR = (HOSTNAME, PORT)

PORT = 443
REQ = "GET / HTTP/1.1\nHost: {}\n\n".format(HOSTNAME).encode("utf-8")
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect((HOSTNAME, PORT))
tcp_sock = ssl.wrap_socket(tcp_sock, keyfile=None,
                           certfile=None, server_side=False,
                           cert_reqs=ssl.CERT_NONE,
                           ssl_version=ssl.PROTOCOL_SSLv23)
tcp_sock.sendall(REQ)
result = tcp_sock.recv(BUFFSIZE).decode("utf-8")
print(result)
result = tcp_sock.recv(BUFFSIZE).decode("utf-8")
print(result)
# for extracting all data:
# while (len(result) > 0):
#     result = tcp_sock.recv(BUFFSIZE).decode("utf-8")
#     print(result)
