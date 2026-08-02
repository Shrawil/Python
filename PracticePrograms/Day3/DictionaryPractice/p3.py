# Reverse Dictionary

a = {
    1:'Apple',
    2:'Banana',
    3:'Cherry',
    4:'Dragon Fruit'
}

rev = {}

for item in a:
    rev[a[item]] = item

print(a)
print(rev)