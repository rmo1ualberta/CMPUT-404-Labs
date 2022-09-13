import socket
import sys
# based on example code from python docs: https://docs.python.org/3/library/socket.html#socket.socket.connect
port = int(sys.argv[1])      # port specified in args
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',port))
sock.listen(1)
conn, addr = sock.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        print(data)
        if not data: break
        conn.sendall(data)

sock.close()
