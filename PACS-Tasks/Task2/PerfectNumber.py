# Check Perfect Number    (Example: 28  1+2+4+7+14=28)

num = int(input("Enter a number : "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i 

print("Perfect number." if sum == num else "Not a perfect number.")