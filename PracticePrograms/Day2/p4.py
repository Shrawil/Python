# Compress a string

s1 = input("Enter a string : ")
count = 1
s2 = ""

print(s1)
for i in range(len(s1)-1):
    if s1[i] == s1[i+1]:
        count += 1
    else:
        s2 += s1[i]
        if count > 1:
            s2 += str(count)
        count = 1
s2 += s1[-1]
if count > 1:
    s2 += str(count)

print(s2)