
from httpServer.handler.base_handler import streamRequestHandler

class BaseHttpRequestHandler(streamRequestHandler):

    def __init__(self, server, request, client_address):
        self.method = None
        self.path = None
        self.version = None
        self.headers = None
        self.body = None
        streamRequestHandler.__init__(server, request, client_address)

    def handle(self):
        try:
            if not self.parse_request():
                return
            method_name = 'do_' + self.method
            if not hasattr(self, method_name):
                return

            method = getattr(self, method_name)
            method()
            self.send()
        except Exception as e:
            print(e)

    def parse_headers(self):
        headers = {}

        while True:
            line = self.readline()
            if line:
                key, value = line.split(":", 1)
                key = key.split()
                value = value.split()
                headers[key] = value
            else:
                break

        return headers

    def parse_request(self):
        first_line = self.rfile.readline()
        words = first_line.split()

        self.method, self.path, self.version = words

        self.headers = self.parse_headers()

        key = 'Content-Length'
        if key in self.headers.keys() :
            body_length = int(self.headers[key])
            self.body = self.read(body_length)

        return True
