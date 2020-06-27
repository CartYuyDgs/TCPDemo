# -*- encoding=utf-8 -*-

from urllib import parse
import json
from httpServer.handler.base_httphandler import BaseHttpRequestHandler
import os
RESOURCES_PATH = os.path.join(os.path.abspath(os.path.dirname(__name__)),"../resources")

class SimpleHTTPRequestHandler(BaseHttpRequestHandler):

    def __init__(self, server, request, client_address):
        BaseHttpRequestHandler.__init__(self, server, request, client_address)
        pass

    def do_GET(self):
        found, resource_path = self.get_resources(self.path)
        if not found:
            self.write_error(404)
            self.send()
        else:
            with open(resource_path, 'rb') as f:
                fs = os.fstat(f.fileno())

                clength = str(fs[6])
                self.write_response(200)
                self.write_header('Content-Length', clength)
                self.end_header()
                while True:
                    buf = f.read(1024)
                    if not buf:
                        break
                    self.write_content(buf)

    def get_resources(self, path):
        url_result = parse.urlparse(path)
        resource_path = str(url_result[2].decode())
        if resource_path.startswith('/'):
            resource_path = resource_path[1:]
        resource_path = os.path.join(RESOURCES_PATH, resource_path)
        if os.path.exists(resource_path) and os.path.isfile(resource_path):
            return True, resource_path
        else:
            return False, resource_path
    def do_POST(self):
        body = json.loads(self.body)

        username = body['username']
        password = body['password']

        if username == 'dongdongqiang' and password == '123456':
            response = {'message':'success', 'code': 0}
        else:
            response = {'message': 'false', 'code': -1}
        response = json.dumps(response)
        self.write_response(200)
        self.write_header('Content-Length', len(response))
        self.end_header()
        self.write_content(response)
