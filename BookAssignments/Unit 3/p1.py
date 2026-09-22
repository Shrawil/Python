# Write a script which takes an integer number from the user as input
# prints all it's divisors (Excluding 1).

n = int(input("Enter a number : "))

for i in range(2, n+1):
    if n % i == 0:
        print(i)