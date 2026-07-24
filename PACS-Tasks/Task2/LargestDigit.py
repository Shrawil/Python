# Find the Largest Digit in a Number (4786 --> largest 8)

num = int(input("Enter a number : "))
temp = num
largest = 0

while num > 0:
    digit = num % 10
    if digit > largest: largest = digit
    num = num // 10

print(f'Largest digit in {temp} is {largest}.')