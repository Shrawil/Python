def findGreatest(*args: int):
    max = args[0]
    for i in args:
        if i > max:
            max = i
    return max

def main():
    n = int(input("Enter number of values you want to enter : "))
    numbers = []
    for i in range(n):
        num = int(input(f"Enter value {i+1} : "))
        numbers.append(num)
    print(f"{findGreatest(*numbers)} is largest!")


if __name__ == '__main__':
    main()