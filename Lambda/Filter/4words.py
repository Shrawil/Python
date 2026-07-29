# Keep only name bigger than 4 characters

names = [
    'Shrawil',
    'Archita',
    'Kriti',
    'Zaid',
    'Ravi',
]

res = list(filter(lambda x : len(x) > 5, names))

print(res)