arr = (1,2,3,4,5,4)

count = 0
flag = True 

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
        if count > 1: 
            flag = False
            break
    count = 0
print('Distinct' if flag else 'Not distinct')