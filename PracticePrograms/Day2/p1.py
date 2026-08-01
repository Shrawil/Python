# Rotate list left by one

ls = [1,2,3,4,5,6]
#    [6,1,2,3,4,5]

print(ls)
ls.insert(0, ls.pop())
print(ls)