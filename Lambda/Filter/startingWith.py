ch = 'S'

words = [
    'Scale',
    'Power',
    'Mouse',
    'Table',
    'Spoon',
    'Spider'
]

res = list(filter(lambda x : x[0].lower() == 's', words))

print(res)