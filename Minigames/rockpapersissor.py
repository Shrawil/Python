import random

choices = ["rock", "paper", "sissor"]

def main() -> None:
    print("Welcome to rock paper sissor!")

    while True:
        pChoice = input("Make your move : ")
        pChoice = pChoice.lower()
        cChoice = random.choice(choices)
        print(f"Bot chose : {cChoice}!")

        if cChoice == pChoice:
            print("It's a Draw")
        elif cChoice == "rock" and pChoice == "paper" or cChoice == "paper" and pChoice == "sissor" or cChoice == "sissor" and pChoice == "rock":
            print("You won!")
        elif cChoice == "rock" and pChoice == "sissor" or cChoice == "paper" and pChoice == "rock" or cChoice == "sissor" and pChoice == "paper":
            print("You lose!")
        else: print("Invalid choice! Choose between Rock Paper Sissor.")

        playAgain = input("Want to play again [y/n] : ")
        if playAgain.lower() == 'n': break
if __name__ == '__main__':
    main()