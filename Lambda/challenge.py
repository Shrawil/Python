students = [
    ("Alice",80),
    ("Bob",95),
    ("John",70),
    ("David",88),
    ("Eva",91)
]

# Student with marks greater than 85
res1 = list(filter(lambda x : x[1] >= 85, students))

# Change format to 'name : marks'
res2 = list(map(lambda x : f'{x[0]} : {x[1]}', students))

# Sort by highest 
res3 = sorted(students, key=lambda x : x[1])

print(res1)
print(res2)
print(res3)