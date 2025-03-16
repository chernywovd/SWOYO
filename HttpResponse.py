class HttpResponse:
    'Класс для представления HTTP-ответа'
    def __init__(self, status_code: int, headers: dict, body: str):
        self.status_code = status_code
        self.headers = headers
        self.body = body

    @classmethod
    def from_bytes(cls, binary_data):
        data = binary_data.decode()
        headers, body = data.split("\r\n\r\n", 1)
        header_lines = headers.split("\r\n")
        status_code = int(header_lines[0].split()[1])
        headers_dict = {}
        for line in header_lines[1:]:
            key, value = line.split(": ", 1)
            headers_dict[key] = value
        return cls(status_code, headers_dict, body)