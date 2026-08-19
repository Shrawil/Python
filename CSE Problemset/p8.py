# Palindrome Reorder
n = input()
myDict = {}
for i in n:
    if n.count(i) == 1 or n.count(i) % 2 == 0:
        myDict[i] = n.count(i)
    else:
        print("Can't form a palindrome.")
        break

res = ""

for i in myDict:
    for j in range((myDict[i])//2):
        res += i

res += res[::-1]
print(res)