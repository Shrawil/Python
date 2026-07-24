import random

WORDS = [
    "trial",
    "denial",
    "acceptance",
    "reject",
    "idea",
    "bottle",
    "base",
    "fire",
    "tower",
    "radio",
    "oval",
    "ladder",
    "rage",
    "egg",
    "giant",
    "tornado",
    "orange",
    "eager",
    "ramp",
    "pineapple",
    "eagle",
    "elephant",
    "telephone",
    "east"
]

def updateHint(word : str, guess : str, hintWord : str) -> str:
    if guess in hintWord:
        print("You have already guessed this letter!")
        return hintWord
    
    print("Letter matched!")
    hintList = list(hintWord)

    for i in range(len(word)):
        if word[i] == guess:
            hintList[i] = guess
            
    return "".join(hintList)

def main() -> None:
    # Choose one random word from WORDS list.
    word = random.choice(WORDS)
    life = 5
    hintWord = "-" * len(word)
    matched = False
    win = False

    print(f"Random word = {word}")

    # To run the game untill the player wins or loses.
    while True:
        print(f"{hintWord} | Life : {life}")
        if hintWord == word:
            win = True
            break

        guess = input("Enter a letter : ").lower()
        if len(guess) > 1:
            print("You can not enter more than one character!")
        else:
            # Compares guess alphabet with each letter in secret word.
            for words in word:
                if guess == words:
                    matched = True

            # Announce whether the letter matches or not.
            if matched: 
                hintWord = updateHint(word, guess, hintWord)
            else:
                print("Wrong guess!") 
                life -= 1
            matched = False

            # Checks whether player has more guesses left or not.
            if life == 0:
                break

    if win: print("You won!")
    else: print("You lose!")

if __name__ == '__main__':
    main()