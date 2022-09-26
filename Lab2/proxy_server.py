import socket, sys
from multiprocessing import Process

host = '127.0.0.1'
target_host = "www.google.com"
port = 8001
buff = 1024


def main():
    # socket for out client
    try:
        sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockClient.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sockClient.bind((host, port))
        sockClient.listen(1)
    except socket.error as e:
        print('ERROR: failed to establish client socket. %s' % e)
        sys.exit(1)


    while True:
        conn, addr = sockClient.accept()
        print('Connected by', addr)
        childProcess = Process(target=childRecvAndSend, args=[conn])
        childProcess.daemon = True
        childProcess.start()

        conn.close()


def childRecvAndSend(conn):

    try:
        fullDataClient = conn.recv(buff)
    except socket.error as e:
        print('ERROR: failed to receive data from client. %s' % e)
        sys.exit(1)
    
    print("Now sending data from client: %s" % fullDataClient)

    # establish socket connection with google.com
    try:
        sockGoogle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockGoogle.connect((target_host,80))
        print("Connected to %s" % target_host)
    except socket.error as e:
        print('ERROR: failed to establish target socket. %s' % e)
        sys.exit(1)

    # now we send the data received from the client to google and then receive it
    try:
        sockGoogle.sendall(fullDataClient)
        sockGoogle.shutdown(socket.SHUT_WR)
    except socket.error as e:
        print('ERROR: failed to send client data to target host. %s' % e)
        sys.exit(1)
        
    # receive the data returned by google
    fullDataGoogle = b""
    try:
        while True:
            dataGoogle = sockGoogle.recv(buff)
            if not dataGoogle:
                break
            fullDataGoogle += dataGoogle
    except socket.error as e:
        print('ERROR: failed to receive data from target host. %s' % e )
        sys.exit(1)


    # send data received from google back to our client
    try:
        conn.sendall(fullDataGoogle)
    except socket.error as e:
        print('ERROR: failed to send target host data to client. %s' %e)
        sys.exit(1)

    sockGoogle.close()



if __name__ == "__main__":
    main()