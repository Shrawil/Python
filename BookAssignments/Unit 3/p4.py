# Ask user for integer n
# Write a script that has the integers from 1 to n-1 as keys and squares as values.

n = int(input("Enter a number : "))
d = dict()

for i in range(1, n+1):
    d[i] = i**2

print(d)