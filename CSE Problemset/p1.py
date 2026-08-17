# Weird Algorithm
# Consider an algorithm that takes as input a positive integer n. 
# If n is even, divide it by two.
# If n is odd, multiply it by 3 and add 1.
# Repeat it until n is 1.

n = int(input())

print(n, end=" ")
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3) + 1
    print(n, end=" ")