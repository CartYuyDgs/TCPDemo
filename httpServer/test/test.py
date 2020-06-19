
from httpServer.socker_server.socket_server import TcpServer
from httpServer.handler.base_handler import streamRequestHandler
import threading
import socket

class SocketServerTest:

    def run_server(self):
        tcp_server = TcpServer(('127.0.0.1', 8888), TestBaseResuestHandler)
        tcp_server.server_forever()

    def gen_client(self, num):
        clients = []
        for i in range(num):
            client_thread = threading.Thread(target=self.client_connect())
            clients.append(client_thread)
        return clients

    def client_connect(self):
        client = socket.socket()
        client.connect(('127.0.0.1',8888))
        client.send(b'hello TcpServer\r\n')
        msg = client.recv(1024)
        print('client rec: ',msg)


    def run(self):
        print("run.....")
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        clients  = self.gen_client(10)
        for client in clients :
            client.start()
        print("start.....")
        server_thread.join()
        for client in clients :
            client.join()
        print("join.....")



class TestBaseResuestHandler(streamRequestHandler):

    def handler(self):
        msg = self.readline()
        print("msg: ",msg)
        self.write_content(msg)
        self.send()
        pass


if __name__ == '__main__':
    SocketServerTest().run()