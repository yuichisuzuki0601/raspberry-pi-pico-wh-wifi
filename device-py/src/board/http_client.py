from ujson import dumps
import urequests
from board.timestamp import jstNow

class HttpClient:
    TIMEOUT = 3#[s]

    def __init__(self, base_url):
        self.base_url = base_url

    def __noop(self, _): pass

    def post(self, path, body, on_success, on_error = __noop):
        print(f'POST {self.base_url}/{path} {jstNow()}')
        try:
            response = urequests.post(
                f'{self.base_url}/{path}',
                data = dumps(body).encode('utf-8'),
                headers = {
                    'Content-Type': 'application/json',
                    'User-Agent': 'raspberry-pi-pico'
                },
                timeout = HttpClient.TIMEOUT
            )
            on_success(response)
            response.close()
        except Exception as e:
            on_error(e)
