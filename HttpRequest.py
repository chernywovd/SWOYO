from urllib.parse import urlparse

class HttpRequest:
    'Класс для представления HTTP-запроса'
    def __init__(self, method: str, url: str, headers: dict, body: str):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def to_bytes(self):
        headers_str = "\r\n".join(f"{k}: {v}" for k, v in self.headers.items())
        request_line = f"{self.method} {urlparse(self.url).path} HTTP/1.1"
        return f"{request_line}\r\n{headers_str}\r\n\r\n{self.body}".encode()