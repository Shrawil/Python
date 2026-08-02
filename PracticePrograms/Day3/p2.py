# Caesar Cipher

a = "Change this"
new = ""

for i in a:
    if i.isalpha():
        new += chr(ord(i)+1)
    else:
        new += i

print(new)