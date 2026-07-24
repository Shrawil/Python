# Check whether a Number is a Strong Number  (Example: 145   1!+4!+5!=145)

num = int(input("Enter a number : "))
copy = num 
res = 0

def factorial(digit: int):
    fact = 1
    for i in range(2, digit+1):
        fact *= i
    return fact

while num > 0:
    digit = num % 10
    res += factorial(digit)
    num = num // 10

print('Strong number.' if copy == res else 'Not a strong number.')