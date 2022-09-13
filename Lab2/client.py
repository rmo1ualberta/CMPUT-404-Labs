import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.google.com", 80))
print(sock)
sock.close()
