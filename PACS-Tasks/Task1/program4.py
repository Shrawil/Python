# Write a python program to reverse the digits of given number

num = int(input("Enter a number : "))
rev = 0
copy = num 

while copy > 0:
    digit = copy % 10
    rev = (rev * 10) + digit
    copy = copy // 10

print(f"{num} reversed is {rev}.")