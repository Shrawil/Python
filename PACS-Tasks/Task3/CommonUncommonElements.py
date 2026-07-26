import Duplicates

# Find common elements.

l1 = [1,2,3,4,5,6,2]
l2 = [1,2,6,7,7]

common = list()
uncommon = list()

for item in l1:
    # We append in common list if item is in 2nd list else append in uncommon list
    if item in l2:
        common.append(item)
    else:
        uncommon.append(item)

# Using a previously made program to remove duplicated in list.
common = Duplicates.removeDuplicates(common)
uncommon = Duplicates.removeDuplicates(uncommon)

print(common)
print(uncommon)