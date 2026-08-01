# Intersection of Lists

a = [1,2,3,4,5,6]
b = [3,4,6]

union = []
intersection = []
subset = True

print(f"{a} ⋃ {b} = ", end="")
for i in a:
    if i not in b:
        union.append(i)
union.extend(b)
print(union)

print(f"{a} ⋂ {b} = ", end="")
for i in a:
    if i in b:
        intersection.append(i)
print(intersection)

print(f"{a} - {b} = ", end="")
subtraction = [i for i in a if i not in b]
print(subtraction)

print(f"{a} ⊂ {b} = ", end="")
for i in a:
    if i not in b:
        subset = False
        break
print(subset)