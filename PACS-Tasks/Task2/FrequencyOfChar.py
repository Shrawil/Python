# Find Frequency of every Character.    (Example apple a :1,p :2,l :1,e :1)

a = 'APPLE'
count = 0

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    print(f'{a[i]} appeared {count} times in {a}.')
    count = 0