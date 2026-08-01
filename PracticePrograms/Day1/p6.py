# Merge two sorted lists
n1 = [1,6,7,10]
n2 = [2,4,5,8]
n3 = []

i = 0
j = 0
while True:
    if i > len(n1)-1 or j > len(n2)-1:
        break
    if n1[i] > n2[j]:
        # print(f'Appending {n2[j]}')
        n3.append(n2[j])
        j += 1
    else:
        # print(f'Appending {n1[i]}')
        n3.append(n1[i])
        i += 1
print(n3)