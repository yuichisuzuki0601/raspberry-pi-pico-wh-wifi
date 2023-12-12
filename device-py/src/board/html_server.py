from usocket import socket, AF_INET, SOCK_STREAM

RESPONSE_HEADER = '''\
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {}\
'''

class HtmlServer():

    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(('', 80))
        self.socket.listen()
        self.handlers = {}

    def add_mapping(self, path, handler):
        self.handlers[path] = handler

    def observe(self): 
        conn, addr = self.socket.accept()

        print(f'=== Got a connection from {addr} ===\n')
        request = conn.recv(1024).decode('utf-8')
        print(request)

        content = ''
        is_html = False

        for path, handler in self.handlers.items():
            if f'GET {path}' in request:
                content, is_html = handler(request)
                break

        if is_html:
            content = f'{RESPONSE_HEADER.format(len(content))}\n\n{content}'

        conn.send(content)
        conn.close()

    def close(self):
        self.socket.close()
