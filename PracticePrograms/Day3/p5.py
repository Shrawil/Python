# Zig Zag Matrix

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

lenA = len(a)
start = 0
stop = lenA
step = 1
for r in range(lenA):
    for c in range(start, stop, step):
        print(a[r][c], end=" ")
    if start == 0:
        start = stop - 1
        stop = -1
        step = -1
    else:
        start = 0
        stop = lenA
        step = 1