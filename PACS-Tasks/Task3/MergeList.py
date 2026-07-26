# Merge two lists.

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

# Method 1
l3 = l1 + l2
print(l3)

# Method 2
l1.extend(l2)
print(l1)