import os

import pytest

path_res = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources'))
path_tmp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp'))


@pytest.fixture(scope='session', autouse=True)
def directory_management():
    files = os.listdir(path_tmp)
    for f in files:
        os.remove(os.path.join(path_tmp, f))
