
import socket

def client():
    s = socket.socket()

    HOST = '127.0.0.1'
    PORT = 8080

    s.connect((HOST,PORT))
    s.send(b"hello ")
    msg = s.recv(1024)
    print("from server : %s" %msg)

if __name__ == '__main__':
    client()