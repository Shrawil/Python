import datetime

class Banking:
    class Transfer:
        deposites = []
        withdrawals = []
        def deposite(self, amount):
            if amount <= 0:
                print("Deposite amount must be greater than 0!")
            self.balance += amount
            self.deposites.append([amount, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")])
            print("Deposited amount : ", amount)

        def withdraw(self, amount):
            if self.balance - amount < 0:
                print("Withdrawal amount can't be greater than current balance!")
                return 
            self.balance -= amount
            self.withdrawals.append([amount, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")])
            print("Withdrawal amount : ", amount)

    class Enquiry:
        def get_withdrawals(self):
            for item in Banking.Transfer.withdrawals:
                print(item)

        def get_deposites(self):
            for item in Banking.Transfer.deposites:
                print(item)

    class Account(Transfer, Enquiry):
        def __init__(self, username:str, age:int, dob:str, password:str):
            self.username = username
            self.age = age
            self.__password = password
            self.dob = dob
            self.balance = 0
            print("Account created!")

        def secret(self):
            secret = "catsarecute"
            password = input("Enter secret pass : ")
            if password != secret:
                return f"Access denied!"
            return f"{self.username}#{self.__password}#{self.age}#{self.dob}#{self.balance}"

        def info(self):
            print(f"Username : {self.username} | Age : {self.age} | DOB : {self.dob} | Balance : {self.balance}")

        def change_username(self, new_username):
            if self.username == new_username:
                print("New username must be different from the current one.")
                return
            self.username = new_username

        def change_password(self, old_password, new_password):
            if self.__password == old_password:
                self.__password = new_password
                return
            print("Incorrect password!")

def createAccount():
    name = input("Enter your username : ")
    age = int(input("Enter your age : "))
    dob = input("Enter your dob [dd-mm-yyyy] : ")
    password = input("Enter your password : ")
    return Banking.Account(name, age, dob, password)

def account_views(User):
    while True:
        choice = int(input("[1] Account info | [2] Change username | [3] Change password | [4] Main menu: "))
        if choice == 1:
            User.info()
        elif choice == 2:
            username = input("Enter new username : ")
            User.change_username(username)
        elif choice == 3:
            old_password = input("Enter current password : ")
            new_password = input("Enter new password : ")
            User.change_password(old_password, new_password)
        elif choice == 4:
            break
        else:
            print("Invalid input received!")

def transfer_views(User):
    while True:
        choice = int(input("[1] Deposite | [2] Withdrawal | [3] Main menu: "))
        if choice == 1:
            amount = int(input("Enter an amount to deposite : "))
            User.deposite(amount)
        elif choice == 2:
            amount = int(input("Enter an amount to withdraw : "))
            User.withdraw(amount)
        elif choice == 3:
            break
        else:
            print("Invalid input received!")
    
def enquiry_views():
    while True:
        choice = int(input("[1] Deposite history | [2] Withdrawal history | [3] Main menu: "))
        if choice == 1:
            User.get_deposites()
        elif choice == 2:
            User.get_withdrawals()
        elif choice == 3:
            break
        else:
            print("Invalid input received!")

print("Let's create your account!")
User = createAccount()

while True:
    choice = int(input("[1] Accounts | [2] Transfer | [3] Enquiry | [4] Exit : "))
    if choice == 1:
        account_views(User)
    elif choice == 2:
        transfer_views(User)
    elif choice == 3:
        enquiry_views(User)
    elif choice == 4:
        break
    elif choice == 69:
        print(User.secret())
    else:
        print("Invalid input received!")