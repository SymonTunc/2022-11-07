from collections import namedtuple

Person = namedtuple('Person', ('firstname', 'lastname'))

csv_content = [
    ['Joerg', 'Faschingbauer'],
    ['Isolde', 'Haubentaucher'],
]

persons = []
for row in csv_content:
    persons.append(Person._make(row))

print(persons)
