import csv

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
