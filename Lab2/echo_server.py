#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        # reuse addr
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            

            childProcess = Process(target=childRecvAndSend, args=[conn])
            childProcess.daemon = True
            childProcess.start()

            conn.close()

def childRecvAndSend(conn):

    #recieve data, wait a bit, then send it back
    fullData = conn.recv(BUFFER_SIZE)
    print(fullData)
    time.sleep(0.5)
    conn.sendall(fullData)
    conn.close()

if __name__ == "__main__":
    main()
