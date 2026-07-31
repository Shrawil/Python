# Bubble Sort
ls = [7,5,8,3,4,31,54,5]
print(ls)

for i in range(len(ls)):
    isSorted = True
    for j in range(len(ls)-1-i):
        if ls[j] > ls[j+1]:
            isSorted = False
            temp = ls[j]
            ls[j] = ls[j+1]
            ls[j+1] = temp 
    if isSorted:
        break
print(ls)