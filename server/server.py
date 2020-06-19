
import socket

def server():
    s = socket.socket()
    HOST = '127.0.0.1'
    PORT = 8080
    s.bind((HOST,PORT))

    s.listen(5)

    while True:
        c, addr = s.accept()
        print("connect client: "+ str(addr))
        msg = c.recv(1024)
        c.send(msg)

if __name__ == '__main__':
    server()