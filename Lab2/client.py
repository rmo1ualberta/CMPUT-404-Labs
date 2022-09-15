import socket

target_host = "www.google.com"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((target_host, 80))

req = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
sock.send(req.encode())

data = sock.recv(1024)
print("The page requested is:")
print(data)
sock.close()
