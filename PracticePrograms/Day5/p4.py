# 5 candies 4 people

candies = 5
people = 4

print(f"Their are {candies} candies and {people} people.")
for i in range(1, candies-(candies-people)+1):
    for j in range(1, people+1):
        if i == j:
            print(f"Person {j} recieved 2 candies.")
        else:
            print(f"Person {j} recieved 1 candy.")
    print()

candies = 4
people = 5

print(f"Their are {candies} candies and {people} people.")
for i in range(1, candies+(people-candies)+1):
    for j in range(1, people+1):
        if i == j:
            print(f"Person {j} recived no candies.")
        else:
            print(f"Person {j} recived 1 candy.")
    print()
