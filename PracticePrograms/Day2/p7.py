# Find Duplicate Elements

ls1 = [1,2,6,5,12,8,9,5,5,3,2,6,5]
ls2 = []
ls1.sort()
print(ls1)
for i in range(len(ls1)-1):
    if ls1[i] == ls1[i+1] and ls1[i] not in ls2:
        ls2.append(ls1[i])
print(ls2)