words = [
    'List',
    'uPpeR',
    'lamBda'
]

upperWords = list(map(lambda x : x.upper(), words))
lowerWords = list(map(lambda x : x.lower(), words))
capWords = list(map(lambda x : x.capitalize(), words))
print(upperWords)
print(lowerWords)
print(capWords)