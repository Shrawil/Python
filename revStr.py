def main():
    myString = input("Enter a string : ")
    print(f"{myString} reversed is ", end="")
    for i in range(len(myString)-1, -1, -1):
        print(myString[i], end="")
    
if __name__ == '__main__':
    main()