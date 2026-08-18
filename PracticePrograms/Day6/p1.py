'''
[1,2,3,4,5]

1x2
1x2x3
1x2x3x4
1x2x3x4x5
2
2x3
2x3x4
2x3x4x5
3
3x4
3x4x5
4
4x5
5
'''
ls = [-2, 3, -4]

best = ls[0]
for i in range(len(ls)):
    temp = 1
    for j in range(i, len(ls)):
        temp *= ls[j]
        best = max(best, temp)
print(best)