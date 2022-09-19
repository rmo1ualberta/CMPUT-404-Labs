import socket,sys

host = '127.0.0.1'
port = 8001
buff = 1024
target_host = "www.google.com"


def main():

    # connect to host socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print("Connected to %s" %host)
    except socket.error as e:
        print("ERROR: failed to establish socket to host. %s" % e)

    req = f"GET / HTTP/1.0\r\nHost: %s\r\n\r\n" % target_host
    send_payload(sock, req)

    # receive and print the data
    full_data = b""
    while True:
        data = sock.recv(buff)
        if not data:
            break
        full_data += data
    print(full_data)

    sock.close()

def send_payload(s, payload):
    try:
        s.sendall(payload.encode())
    except socket.error:
        print("Error: sending payload failed", file=sys.stderr)
        sys.exit()

if __name__ == "__main__":
    main()