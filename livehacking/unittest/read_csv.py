import csv

def read(filename):
    users = []

    f = open(filename)
    rdr = csv.reader(f)
    for id, firstname, lastname in rdr:
        user = {
            'id': int(id),
            'firstname': firstname,
            'lastname': lastname,
            }
        users.append(user)
        
    return users
