t1 = (1,4,6,4,3,8,6)
t2 = (4,3,2,4,4)

r = min(len(t1), len(t2))

t1t2 = 0
for i in range(r):
    t1t2 += t1[i]*t2[i]

print(t1t2)