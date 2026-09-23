# Write a script which prints all numbers between 1 to 100 such that all the digits are even.
# Example: 2, 4, 6, 8, 20, 22, 24, 26 etc... 10 is excluded because 1 is odd.

def allEven(i):
    while i != 0:
        digit = i % 10
        if digit % 2 != 0:
            return False
        i = i // 10
    return True

for i in range(1, 101):
    if allEven(i):
        print(i)