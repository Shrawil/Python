# Removing duplicates.
def removeDuplicates(ls):
    noDup = [ls[0]]
    for item in ls[1:]:
        if item != noDup[-1]:
            noDup.append(item)
    return noDup

# Count duplicate elements.
def countDuplicates(ls):
    visited = ''
    dupElem = 0
    for item in ls:
        if str(item) in visited:
            dupElem += 1
        visited += str(item)
    return dupElem

def main():
    ls = [1,2,2,3,5,5,5,6,7]
    l1 = removeDuplicates(ls)
    count = countDuplicates(ls)
    print(f'Number of duplicated in {ls} is {count}.')
    print(f'Duplicated removed list : {l1}.')


if __name__ == '__main__':
    main()