# Remove duplicate elements

n1 = [1,1,2,2,3,4,4,4,5,6,7,7,7]
n2 = []

for i in range(len(n1)-1):
    if n1[i] != n1[i+1]:
        n2.append(n1[i])

print(n1, n2)