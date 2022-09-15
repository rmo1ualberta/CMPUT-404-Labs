import socket,sys

host = '127.0.0.1'
port = int(sys.argv[1])      # port specified in args

# first socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.sendall(b"Bruh")
data = sock.recv(1024)

print('Received data: \n')
print(data)

sock.close()