import socket, sys

host = '127.0.0.1'
target_host = "www.google.com"
port = int(sys.argv[1])      # port specified in args

# first socket
sockGoogle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockGoogle.connect((target_host,80))
print("Connected to %s" % target_host)

# socket for out client
sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockClient.bind((host, port))
sockClient.listen(1)
conn, addr = sockClient.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        print("Now sending data from client: %s" % data)

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
        dataGoogle = sockGoogle.recv(1024)
        print(dataGoogle)

        # send data received from google back to our client
        conn.sendall(dataGoogle)
        if not data or not dataGoogle: break
    

sockGoogle.close()
sockClient.close()