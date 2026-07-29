def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)

fact = factorial(5)
print(fact)