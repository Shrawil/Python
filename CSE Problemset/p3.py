dna = input()

max = 1
count = 1

for i in range(len(dna)-1):
    if dna[i] == dna[i+1]:
        count += 1
    else:
        count = 1
    if max < count:
        max = count
print(max)    