# Write a python program to convert binary number to its decimal equivalent.

# Example - 1101
# 1 1 0 1
# 8 4 2 1

# Flag to keep track whether the number entered is valid or not.
flag = True
binary = input("Enter binary number : ")

# Try exept block to check if user entered a valid binary number or not, exits the program if not.
try:
    num = int(binary)
except ValueError:
    print("Invalid binary number received.")
    exit()

# Variable to store the result.
decimal = 0

power = 1

# Loop to iterate till all digits in binary number is visited.
for _ in range(len(binary)):
    # Take the last digit of num.
    digit = num % 10

    # Breaks out of loop if we detect any other number than 1 and 0 and sets the flag to False.
    if digit > 1:
        flag = False
        break

    # Multiplies the power based on the position of individual binary digit and adds it to result.
    decimal += power * digit

    # Removes the digit taken.
    num = num // 10

    # Moves to next power.
    power *= 2

if flag:
    print(f"{binary} = {decimal}")
else:
    print("Not a valid binary number.")