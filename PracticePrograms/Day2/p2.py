# Binary Search

ls = [1,2,3,4,5,6]
elem = int(input(f"Enter a number to find index of in {ls} : "))

left = 0
right = len(ls)-1
found = False

while left < right:
    mid = (left+right)//2
    if ls[mid] == elem:
        found = True
        break
    elif ls[mid] > elem:
        right = mid - 1
    else:
        left = mid + 1

if found:
    print(f"Element {elem} found at index {mid}!")
else:
    print(f"Element {elem} not found!")