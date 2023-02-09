
from configparser import ConfigParser

from http.server import BaseHTTPRequestHandler, HTTPServer

server_address = ('0.0.0.0', 8000)

with open('example-server/example-data.txt', 'r') as f:
    config = ConfigParser()
    config.read_file(f)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route, query = self.path.split('?')
        route = route.strip('/')
        member_id = query[query.index('=') + 1:]
        print(route, member_id)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        self.wfile.write(config.get(member_id, route).encode())

if __name__ == "__main__":
    server = HTTPServer(server_address, RequestHandler)
    server.serve_forever()
