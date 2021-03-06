

class BaseRequestHandler:

    def __init__(self, server ,request, client_address):
        self.server = server
        self.request = request
        self.client_address = client_address

    def handler(self):
        pass


class streamRequestHandler(BaseRequestHandler):

    def __init__(self, server, request, client_address):
        BaseRequestHandler.__init__(self, server, request, client_address)

        self.wbuf = []
        self.rfile = self.request.makefile('rb')
        self.wfile = self.request.makefile('wb')

    #编码 字符串-->字节码
    def encode(self, msg):
        if not isinstance(msg, bytes):
            msg = bytes(msg, encoding='utf-8')
        return msg

    #字节码--》字符串
    def decode(self, msg):
        if isinstance(msg, bytes):
            msg = msg.decode()
        return msg

    def read(self, length):
        msg = self.rfile.read(length)
        return self.decode(msg)

    def readline(self, length=65536):
        msg = self.rfile.readline(length).strip()
        return self.decode(msg)

    def write_content(self, msg):
        msg = self.encode(msg)
        self.wbuf.append(msg)
        pass

    def send(self):
        for line in self.wbuf :
            self.wfile.write(line)

        self.wfile.flush()
        self.wfile = []

    def close(self):
        self.wfile.close()
        self.rfile.close()

