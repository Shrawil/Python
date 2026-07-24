print("Simple python calculator")

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

opr = input("Enter an operation to perform [+,-,/,*] : ")

if opr == '+':
    print(f"{num1} {opr} {num2} = {int(num1+num2)}")
elif opr == '-':
    print(f"{num1} {opr} {num2} = {int(num1-num2)}")
elif opr == '*':
    print(f"{num1} {opr} {num2} = {int(num1*num2)}")
elif opr == '/':
    print(f"{num1} {opr} {num2} = {int(num1/num2)}")