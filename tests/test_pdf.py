from pypdf import PdfReader
import os
from .conftest import path_res


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_pdf():
    reader = PdfReader(os.path.join(path_res, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)
    assert number_of_pages == 464
    assert 'pytest' in text
