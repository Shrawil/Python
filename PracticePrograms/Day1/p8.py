# Selection Sort

ls = [4,32,7,5,99,12,10]
print(ls)
# Iterate 
# Choose smallest element
# Put it at i (starting with i = 0 increment each iteration)
for i in range(len(ls)):
    # Assume first element to be smallest
    min = i
    for j in range(i+1, len(ls)):
        if ls[j] < ls[min]:
            min = j
    if min != j:
        temp = ls[j]
        ls[j] = ls[min]
        ls[min] = temp
print(ls)