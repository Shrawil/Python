# Find Frequency of every Character.    (Example apple a :1,p :2,l :1,e :1)

str1 = input("Enter a string : ")
visited = ''

for i in str1:
    if i not in visited:
        print(i, str1.count(i))
        visited += i

'''
a = 'APPLE'
count = 0

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    print(f'{a[i]} appeared {count} times in {a}.')
    count = 0
'''