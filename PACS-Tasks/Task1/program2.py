# Write a python program to find factorial of given number.

num = int(input("Enter a number : "))
copy = num
fact = 1
while copy > 1:
    fact *= copy
    copy -= 1
print(f"Factorial of {num} is {fact}!")