import socket
from urllib.parse import urlparse
from HttpResponse import HttpResponse

def send_http_request(request):
    'Функция для отправки HTTP-запроса через сокет'
    parsed_url = urlparse(request.url)
    host = parsed_url.hostname
    port = parsed_url.port or 80

    #Создание сокета и подключение к серверу
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(request.to_bytes())
        response = sock.recv(4096)
        return HttpResponse.from_bytes(response)