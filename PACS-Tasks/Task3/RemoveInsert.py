# Remove a specific element.

ls = [1,2,3,4,5,6]
print(ls)
item = int(input("Enter an element to remove : "))
ls.remove(item)
print(ls)

item = int(input("Enter an element to insert : "))
idx = int(input(f"Enter index to insert {item} : "))
ls.insert(idx, item)
print(ls)