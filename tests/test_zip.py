from zipfile import ZipFile, ZIP_DEFLATED
from .conftest import path_res
from .conftest import path_tmp
import os.path


def test_zip():
    with ZipFile(os.path.join(path_tmp, 'metanit.zip'), "a", compression=ZIP_DEFLATED, compresslevel=3) as myzip:
        myzip.write(os.path.join(path_res, 'docs-pytest-org-en-latest.pdf'))
        myzip.write(os.path.join(path_res, 'users.csv'))
        myzip.write(os.path.join(path_res, 'file_example_XLSX_50.xlsx'))

        for item in myzip.infolist():
            assert item.file_size == os.path.getsize(os.path.join(path_res, os.path.basename(item.filename)))
            assert os.path.basename(item.filename) == os.path.basename(
                os.path.join(path_res, os.path.basename(item.filename)))
