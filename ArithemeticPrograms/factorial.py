def main():
    num = int(input("Enter a number to find factorial of : "))
    copy = num
    fact = 1
    while copy > 1:
        fact *= copy
        copy -= 1
    print(f"Factorial of {num} is {fact}!")

if __name__ == '__main__':
    main()