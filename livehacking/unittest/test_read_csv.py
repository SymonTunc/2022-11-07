import read_csv

import pytest
import os


@pytest.fixture
def a_file(tmpdir):
    filename = tmpdir/'file.csv'
    with open(filename, 'w') as f:
        users = [
            [1, 'Joerg', 'Faschingbauer'],
            [2, 'Caro', 'Faschingbauer'],
        ]
        for id, firstname, lastname in users:
            f.write(f'{id},{firstname},{lastname}\n')

    yield filename

    os.unlink(filename)

def test_basic(a_file):
    users = read_csv.read(a_file)
    assert len(users) == 2

def test_id_is_int(a_file):
    users = read_csv.read(a_file)
    joerg = users[0]
    assert joerg['id'] == 1
