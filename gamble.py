import random

def runGamble(int: bal, int: diff):
    while True:
        try:
            betAmount = int(input("Enter an amount to bet : "))
            if betAmount > 0 and betAmount <= bal:
                break
            else:
                print("Bet amount should be greater than 0 and and smaller than or equal to your current ballance!")
    if diff == 1:
        if randInt(1, 50) < 50:
            bal 
    

def gamble(int: balance):
    print("Choose difficulty : ")
    print("[1] Easy (Probability : 50% | x2)")
    print("[2] Medium (Probability : 30% | x3)")
    print("[3] Hard (Probability : 10% | x5)")
    print(f"[4] Feeling lucky (Probability : 1% | x10)")
    choice : int
    
    # To make sure user only enters an integer
    while True:
        try:
            choice = int(input(">"))
            break
        except TypeError:
            print("Please enter a valid integer.")
    if choice <= 4 or choice >= 1 and balance > 0:
        runGamble(balance, difficulty)
    
def main(int: choice):
    balance = 0
    print("Welcome to gamble.py!")
    while True:
        print("[1] Gamble | [2] Balance | [3] Exit")\
        choice = int(input(">"))
        if choice == 1:
            gamble(balance)
        elif choice == 2:
            checkBalance()
        elif choice == 3:
            break
        else: 
            print("Invalid input recieved!")
    

if __name__ == '__main__':
    choice = 1
    main(choice)
