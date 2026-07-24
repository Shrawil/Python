# Find the Smallest Digit in a Number (4786 --> 4)

num = int(input("Enter a number : "))
temp = num
smallest = 9

while num > 0:
    digit = num % 10
    if digit < smallest: smallest = digit
    num = num // 10

print(f'Smallest digit in {temp} is {smallest}.')