import random

def runGamble(bal, diff):
    cur = bal
    while True:
        try:
            betAmount = int(input("Enter an amount to bet : "))
            if betAmount > 0 and betAmount <= bal:
                break
            else:
                print("Bet amount should be greater than 0 and smaller than or equal to your current ballance!")
        except ValueError:
            print("Please enter a valid integer!")
    num = random.randint(1, 101)
    if diff == 1:
        if num <= 50: bal += betAmount * 2
        else: bal -= betAmount
    elif diff == 2:
        if num <= 30: bal += betAmount * 3
        else: bal -= betAmount
    elif diff == 3:
        if num <= 10: bal += betAmount * 5
        else: bal -= betAmount
    elif diff == 4:
        if num == 1: bal += betAmount * 10
        else: bal -= betAmount
    if cur > bal:
        print(f"You lost! -{betAmount}")
    else:
        print(f"You won! +{cur}")
    return bal
    

def gamble(balance):
    print("Choose difficulty : ")
    print("[1] Easy (Probability : 50% | x2)")
    print("[2] Medium (Probability : 30% | x3)")
    print("[3] Hard (Probability : 10% | x5)")
    print(f"[4] Feeling lucky (Probability : 1% | x10)")
    print("[5] Home")
    # To make sure user only enters an integer
    while True:
        try:
            difficulty = int(input(">"))
            if difficulty > 5 or difficulty < 1:
                print("Please choose between 1-5!")
            elif balance <= 0:
                print("You don't have enough money to enter!")
                break
            elif difficulty == 5:
                return balance
            else:
                return(runGamble(balance, difficulty))
        except ValueError:
            print("Please enter a valid integer.")
    return balance
    
def checkBalance(balance):
    print(f"Current balance : {balance}.")

def main(choice):
    balance = 1000
    print("Welcome to gamble.py!")
    while True:
        try:
            print("[1] Gamble | [2] Balance | [3] Exit")
            choice = int(input(">"))
            if choice == 1:
                balance = gamble(balance)
            elif choice == 2:
                checkBalance(balance)
            elif choice == 3:
                break
            else: 
                print("Invalid input recieved!")
        except ValueError:
            print("Please enter a valid interger!")

if __name__ == '__main__':
    choice = 1
    main(choice)
