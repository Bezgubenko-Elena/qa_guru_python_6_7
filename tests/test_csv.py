import csv
import os
from .conftest import path_res


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_csv():
    with open(os.path.join(path_res, 'users.csv'), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(os.path.join(path_res, 'users.csv')) as csvfile:
        csvreader = csv.reader(csvfile)
        count_rows = 0
        for row in csvreader:
            if len(row) > 0:
                count_rows += 1
        assert count_rows == 2
