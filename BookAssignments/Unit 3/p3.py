# Write a script which prints all numbers between 1000 and 2000 (Both included)
# and the numbers are divisible by 11 but not divisible by 6.

count = 0
for i in range(1000, 2000+1):
    if i % 11 == 0 and i % 6 != 0:
        count += 1
        print(i)
print(f"Total numbers from 1000 to 2000 that are divisible by 11 but not by 6 are {count}.")