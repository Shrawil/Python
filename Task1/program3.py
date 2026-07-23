# Write a python program to find sum of digits of given number.

num = int(input("Enter a number : "))
copy = num
sum = 0
while copy != 0:
    digit = copy % 10
    sum += digit 
    copy = copy // 10
print(f"Sum of digits in {num} is {sum}.")