# Write a python program to print Fibonacci series up to n terms, where value of n is entered by user.

prev = 0
cur = 1
num = int(input("Enter a number : "))
for i in range(num):
    print(prev)
    nextNum = cur + prev
    prev = cur 
    cur = nextNum