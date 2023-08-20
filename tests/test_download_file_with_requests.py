import os.path
from .conftest import path_tmp
import requests


# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь


def test_download_requests():
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    response = requests.get(url)
    with open(os.path.join(path_tmp, 'selenium_logo.png'), 'wb') as file:
        file.write(response.content)

    size = os.path.getsize(os.path.join(path_tmp, 'selenium_logo.png'))
    assert size == 30803
