# Search an element in a list.
# Find the index of an element.

ls = [1,2,3,4,5,6,7]
print(ls)
item = int(input("Enter an item to search in ls : "))
# Searching in list.
if item in ls:
    # Finding the index too.
    print(f"{item} found at index {ls.index(item)}.")
else:
    print(f"{item} not found!")