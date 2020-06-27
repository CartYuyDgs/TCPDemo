
from httpServer.socker_server.socket_server import TcpServer


class BaseHttpServer(TcpServer):

    def __init__(self, server_address, handler_class):
        self.server_name='BaseHttpserver'
        self.version = 'v0.1'
        TcpServer.__init__(self, server_address, handler_class)