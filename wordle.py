import sqlite3
import random

conn = sqlite3.connect("score.db")
cursor = conn.cursor()

try:
    print("Checking if Score DataBase exists...")
    cursor.execute("CREATE TABLE SCORE(id INTEGER PRIMARY KEY AUTOINCREMENT, playerName varchar(10), wins INT, loses INT)")
    conn.connect()
    print("No DataBase found! Creating one...")
except:
    print("Score DataBase already exits!")

words = [
    "mango", 
    "banana", 
    "pie", 
    "task", 
    "score", 
    "bottle",
    "word",
    "apple",
    "cookie",
    "food",
    "brazil",
    "japan",
    "india",
    "octopus",
    "angel",
    "devil",
    "human",
    "laptop",
    "table",
    "press",
    "circuit",
    "building",
    "bulb",
    "light",
    "lamp",
    "electricity",
    "hour",
    "glass",
    "grass",
    "time",
    "watch",
    "cup",
    "plate",
    "place",
    "analog",
    "remote",
    "job",
    "television",
    "money",
    "data",
    "text",
    "temple",
    "ground",
    "battery",
    "bat",
    "rat",
    "potato",
    "night",
    "day"
]

def play():
    name = input("Enter your name : ")
    cursor.execute("SELECT * FROM SCORE WHERE playerName = ?", (name,))
    player = cursor.fetchone()

    if player is None:
        #No data found so we create one
        cursor.execute("INSERT INTO SCORE(playerName, wins, loses) VALUES(?, ?, ?)", (name, 0, 0))
        conn.commit()
        cursor.execute("SELECT * FROM SCORE WHERE playerName = ?", (name,))
        player = cursor.fetchone()

    playerId = player[0]
    wins = player[2]
    loses = player[3]

    won = False
    maxGuess = 5
    guesses = 0
    word = random.choice(words)
    hint = ["-"] * len(word)

    while True:
        print(f"{hint} | Guesses : {maxGuess - guesses}")
        guesses += 1
        try:
            guess = input("Enter your guess : ")
            if len(guess) == len(word):
                if guess == word: 
                    won = True
                    break
                elif guesses > maxGuess:
                    break
                for i in range(len(word)):
                    if word[i] == guess[i]:
                        hint[i] = "G"
                    elif guess[i] in word:
                        hint[i] = "Y"
                    else: hint[i] = "X"
            else:
                guesses -= 1
                print(f"Your guess should be {len(word)} characters long!")
        except:
            print("Something went wrong, try again!")
    if won:
        print(f"You won! The word was {word}!")
        cursor.execute("UPDATE SCORE SET wins = ? WHERE id=?", (wins+1, playerId))
        conn.commit()
    else:
        print(f"You lose! The word was {word}!")
        cursor.execute("UPDATE SCORE SET loses = ? WHERE id=?", (loses+1, playerId))
        conn.commit()

def showScore():
    cursor.execute("SELECT * FROM SCORE")
    i = 1
    for line in cursor.fetchall():
        print(f"{i}: {line}")
        i += 1

def delScore():
    num = int(input("Enter Player ID to remove [0 to delete all] : "))
    if num == 0:
        cursor.execute("DELETE FROM SCORE")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='SCORE'")
        conn.commit()
        print("All data erased!")
    else:
        cursor.execute("DELETE FROM SCORE WHERE id = ?", (num,))
        conn.commit()
        print(f"Deleted record for player with id {num}!")
while True:
    print("[1] Play | [2] Scoreboard | [3] Delete Record | [0] Exit\n")
    try:
        choice = int(input("Enter your choice : "))
        if choice == 1:
            play()
        elif choice == 2:
            showScore()
        elif choice == 3:
            delScore()
        elif choice == 0:
            break
    except:
        print("Something went wrong, try again!")
print("Thanks for playing!")