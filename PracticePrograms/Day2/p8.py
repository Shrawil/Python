# Check if List is Sorted

ls = [1,2,3,4,5,9,7]
isSorted = True
for i in range(len(ls)-1):
    if ls[i] > ls[i+1]:
        isSorted = False 
if isSorted:
    print("List is sorted!")
else:
    print("List is not sorted!")