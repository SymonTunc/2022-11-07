import csv
from collections import namedtuple

def read_csv_noheader(filename):
    users = []

    f = open(filename, encoding='cp1252')
    rdr = csv.reader(f, delimiter=';', quotechar='"')
    for id, firstname, lastname, birth in rdr:
        ud = {
            'id': int(id),
            'firstname': firstname,
            'lastname': lastname,
            'birth': birth,
        }
        users.append(ud)

    return users

def read_csv_header(filename):
    users = []

    f = open(filename, encoding='cp1252')
    rdr = csv.DictReader(f, delimiter=';', quotechar='"')
    for ud in rdr:
        id = ud['ID']
        firstname = ud['First name']
        lastname = ud['Last name']
        birth = ud['Date of Birth']

        my_ud = {
            'id': int(id),
            'firstname': firstname,
            'lastname': lastname,
            'birth': birth,
        }
        users.append(my_ud)

    return users

Person = namedtuple('Person', ('id', 'firstname', 'lastname', 'birth'))
    
def read_noheader_person(filename):
    persons = []

    f = open(filename, encoding='cp1252')
    rdr = csv.reader(f, delimiter=';', quotechar='"')
    for id, firstname, lastname, birth in rdr:
        persons.append(Person(
            id=int(id),
            firstname=firstname,
            lastname=lastname,
            birth=birth
        ))

    return persons
