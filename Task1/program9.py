# Write a python program to check given number is Armstrong or not.

# 123 -> 1^3 + 2^3 + 3^3 should be equal to 123

num = int(input("Enter a number : "))
power = len(str(num))
copy = num 
sum = 0
while copy != 0:
    digit = copy % 10
    sum += (digit ** power)
    copy = copy // 10
if sum == num:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")