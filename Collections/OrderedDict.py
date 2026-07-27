from collections import OrderedDict

students = OrderedDict()

students['name'] = 'Shrawil'
students['age'] = 19

print(students)
print(students['name'])
print(students['age'])

# Change the order of field in dictionary.
students.move_to_end('name')
print(students)