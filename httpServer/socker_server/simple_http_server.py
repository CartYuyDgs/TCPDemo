
from httpServer.socker_server.base_http_server import TcpServer
from httpServer.handler.simple_http_handler import SimpleHTTPRequestHandler

class SimpleHTTPServer(TcpServer):

    def __init__(self, server_address, handler_class):
        self.server_name = 'SimpleHttpserver'
        self.version = 'v0.1'
        TcpServer.__init__(self, server_address, handler_class)



if __name__ == '__main__':
    SimpleHTTPServer(('127.0.0.1',8888), SimpleHTTPRequestHandler).server_forever()