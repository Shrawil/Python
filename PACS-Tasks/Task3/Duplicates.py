# Remove duplicate elements.
# Count duplicate elements.

ls = [1,2,2,3,5,5,5,6,7]

# Removing duplicates.
noDup = [ls[0]]

for item in ls[1:]:
    if item != noDup[-1]:
        noDup.append(item)
print(ls, noDup)

visited = ''
dupElem = 0
for item in ls:
    if str(item) in visited:
        dupElem += 1
    visited += str(item)

print(f"Number of duplicate elements in {ls} is {dupElem}.")