import asyncio
from ParserArgs import parse_args
from HttpRequest import HttpRequest
from HttpResponse import HttpResponse
from SendHttpRequest import send_http_request
import toml
# import debugpy
import toml
import base64
import json
from urllib.parse import urlparse
import logging
import sys



async def main():
    logging.basicConfig(
        level=logging.INFO,  # Уровень логирования (INFO, DEBUG, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s",  # Формат сообщений
        handlers=[
            logging.FileHandler("./sms_service.log"),  # Логи в файл
            logging.StreamHandler(sys.stdout)  # Логи в консоль
        ]
    )

    if await parse_args() is not False:
        try:
            config = toml.load("config.toml")
            sms_service = config["sms_service"]
        except Exception as ex:
            logging.error(f"\nОшибка загрузки конфигурации: {ex}\n")
            return

        url = sms_service['url']
        username = sms_service['username']
        password = sms_service['password']

        request_body = await parse_args()

        logging.info(f"\nПереданные параметры: {request_body}\n")

        headers = {
            "Host": f"{urlparse(url).hostname}",
            "Content-Type": "application/json",
            "Authorization": f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"
        }

        request = HttpRequest(
            method="POST",
            url=f"{url}/send_sms",
            headers=headers,
            body=json.dumps(request_body)
        )

        response = send_http_request(request)

        print(f"Код ответа: {response.status_code}\n")
        print(f"Тело ответа: {response.body}\n")
        logging.info(f"\nКод ответа: {response.status_code}")


if __name__ == '__main__':
    asyncio.run(main())