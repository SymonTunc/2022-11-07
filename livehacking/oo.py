class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def say_hello(self):
        return f'Hello my name is {self.firstname} {self.lastname}'

    @classmethod
    def make_child(cls, firstname, person1, person2):
        child = cls(firstname, person1.lastname + '-' + person2.lastname)
        return child

joerg = Person('Joerg', 'Faschingbauer')
isi = Person('Isolde', 'Haubentaucher')
print(joerg.say_hello())
print(isi.say_hello())


child = Person.make_child('Alex', joerg, isi)
print(child.say_hello())
