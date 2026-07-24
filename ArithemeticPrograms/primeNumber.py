a = int(input("Enter a number to find factorial of : "))

# We assume the number is prime by default
pole = True

# Start from 2 and go upto a.
for i in range(2, a):
    # If a's remainder become 0 it mean the number is not a prime number.
    if a % i == 0:
        pole = False
        break

if pole:
    print(f"{a} is a prime number.")
else:
    print(f"{a} is not a prime number.")