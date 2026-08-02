# Matrix Rotation (2D Lists)
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
b = []
for c in range(len(a)):
    temp = []
    for r in range(len(a)-1,-1, -1):
        temp.append(a[r][c])
    b.append(temp)
print(a, b)