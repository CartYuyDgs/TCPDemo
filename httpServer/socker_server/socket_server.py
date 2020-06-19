
import socket

class TcpServer():

    #初始化
    def __init__(self, server_address, handler_class):
        self.ServerAddress = server_address
        self.HandlerClass = handler_class
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_down  = False

    # 启动
    def server_forever(self):
        self.Socket.bind(self.ServerAddress)
        self.Socket.listen(10)
        # while True:
        while not self.is_down:
            request, client_address = self.get_request()
            try:
                self.process_request(request, client_address)
            except Exception as e:
                print("err: "+ str(e))
            finally:
                self.close_request(request)

    # 获取请求
    def get_request(self):
        return self.Socket.accept()


    # 处理请求
    def process_request(self, request, client_address):
        handler = self.HandlerClass(self, request,client_address)
        handler.handler()
        pass

    # 关闭请求
    def close_request(self, request):
        request.shutdown(socket.SHUT_WR)
        request.close()

    # 关闭server
    def shutdown(self):
        self.is_down = True
        pass
