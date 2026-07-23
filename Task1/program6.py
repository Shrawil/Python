# Write a python program to check given number is prime or not.

num = int(input("Ente a number : "))
flag = True 
for i in range(2, num):
    if num % i == 0:
        flag = False 
        break 
if flag:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")