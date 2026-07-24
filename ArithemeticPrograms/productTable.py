def main():
    num = int(input("Enter a number for product table : "))
    for i in range(10):
        print(f"{num} x {i+1} = {num*(i+1)}")

if __name__ == '__main__':
    main()