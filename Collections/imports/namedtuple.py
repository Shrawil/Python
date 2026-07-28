from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'email'])
print(Person)

p1 = Person('Shrawil', 18, 'shrawil@gmail.com')
print(p1)
print(p1.name, p1.age, p1.email)