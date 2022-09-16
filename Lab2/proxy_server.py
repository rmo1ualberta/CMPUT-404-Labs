import socket, sys
from multiprocessing import Process

host = '127.0.0.1'
target_host = "www.google.com"
port = int(sys.argv[1])      # port specified in args


def main():
    # socket for out client
    sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockClient.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockClient.bind((host, port))
    sockClient.listen(1)


    while True:
        conn, addr = sockClient.accept()
        print('Connected by', addr)

        childProcess = Process(target=childRecvAndSend, args=[conn])
        childProcess.daemon = True
        childProcess.start()

        conn.close()

def childRecvAndSend(conn):

    data = conn.recv(1024)
    print("Now sending data from client: %s" % data)

    # first socket
    sockGoogle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockGoogle.connect((target_host,80))
    sockGoogle.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Connected to %s" % target_host)

    # now we send the data received from the client to google and then receive it

    # https://stackoverflow.com/questions/28670835/python-socket-client-post-parameters
    headers = """\
    POST /auth HTTP/1.1\r
    Content-Type: {content_type}\r
    Content-Length: {content_length}\r
    Host: {host}\r
    Connection: close\r
    \r\n"""

    body = str(data)                                
    body_bytes = body.encode('ascii')
    header_bytes = headers.format(
        content_type="application/x-www-form-urlencoded",
        content_length=len(body_bytes),
        host=str(host) + ":" + str(port)
    ).encode('iso-8859-1')

    payload = header_bytes + body_bytes

    sockGoogle.send(payload)

    fullDataGoogle = b""
    while True:
        dataGoogle = sockGoogle.recv(1024)
        if not dataGoogle:
            break
        fullDataGoogle += dataGoogle

    print(fullDataGoogle)

    # send data received from google back to our client
    conn.sendall(fullDataGoogle)
    conn.close()
    sockGoogle.close()

if __name__ == "__main__":
    main()