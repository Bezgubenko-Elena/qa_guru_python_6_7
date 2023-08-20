import time

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os.path
from .conftest import path_tmp


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp


def test_download_browser():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": path_tmp,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()), options=options)

    browser.config.driver = driver
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)

    assert os.path.exists(os.path.join(path_tmp, 'pytest-main.zip'))
