import socket,sys

host = '127.0.0.1'
port = int(sys.argv[1])      # port specified in args
buff = 1024

# first socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.sendall(b"Bruh")

full_data = b""
while True:
    data = sock.recv(buff)
    if not data:
        break
    full_data += data
print('Received data: \n')
print(full_data)

sock.close()