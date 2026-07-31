# Count vowels

VOWELS = ['a', 'e', 'i', 'o', 'u']

s = 'MONEye'

count = 0
for i in s:
    if i.lower() in VOWELS:
        count += 1

print(f"There are {count} vowels in {s}.")