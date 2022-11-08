import read_csv

import unittest
import os

seq = 0


class MyTestCase(unittest.TestCase):
    def setUp(self):
        global seq

        users = [
            [1, 'Joerg', 'Faschingbauer'],
            [2, 'Caro', 'Faschingbauer'],
        ]

        self.filename = f'/tmp/file-{seq}.csv'
        seq += 1

        with open(self.filename, 'w') as f:
            for id, firstname, lastname in users:
                f.write(f'{id},{firstname},{lastname}\n')

    def tearDown(self):
        os.unlink(self.filename)

    def test_basic(self):
        users = read_csv.read(self.filename)
        self.assertEqual(len(users), 2)

    def test_id_is_int(self):
        users = read_csv.read(self.filename)
        joerg = users[0]
        self.assertEqual(joerg['id'], '1')

s = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
unittest.TextTestRunner().run(s)
