import time

sen = input("Enter a sentence : ")

res = ""

for i in sen:
    if i.isupper():
        for j in range(65, 91):
            if i == chr(j):
                res += chr(j)
            print(res)
            time.sleep(0.1)
    elif i.islower():
        for j in range(97, 123):
            if i == chr(j):
                res += chr(j)
            print(res)
            time.sleep(0.1)
    elif i == " ":
        res += " "
