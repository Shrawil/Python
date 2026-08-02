# Find Maximum Value (without using max())

a = {
    'A':100,
    'B':200,
    'C':50,
    'D':89
}

for item in a.items():
    maxVal = item
    minVal = item
    break

for item in a.items():
    if item[1] > maxVal[1]:
        maxVal = item
    elif item[1] < minVal[1]:
        minVal = item

print(f"{maxVal[0]} - {maxVal[1]} is maximum.")
print(f"{minVal[0]} - {minVal[1]} is minimum.")