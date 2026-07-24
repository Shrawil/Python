# Print all Prime Numbers between 1–100

def is_prime(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(1, 101):
    if is_prime(i):
        print(i)