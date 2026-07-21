print("# Normal loop - Starts from 0 and goes to (range-1).")
print("for i in range(10):\n\tprint(i, end=\"\")")
for i in range(10):
    print(i, end="")
print("\n")

print("# Start and End defined loop, end is exclusive so it will got to end-1.")
print("for i in range(1, 10):\n\tprint(i, end=\"\")")
for i in range(0, 10):
    print(i, end="")
print("\n")

print("# Start, End, Step (Adds n number to current iteration).")
print("for i in range(1, 11, 2):\n\tprint(i, end=\"\")")
for i in range(0, 10, 2):
    print(i, end="")
print("\n")

print("# Reverse counting.")
print("for i in range(11, 1, -1):\n\tprint(i, end=\"\")")
for i in range(9, -1, -1): 
    print(i, end="")
print("\n")

print("# Reverse counting with gaps.")
print("for i in range(20, 0, -2):\n\tprint(i, end=\"\")")
for i in range(9, -1, -2):
    print(i, end="")
print("\n")

print("# Print letters.")
WORD = "HELLO WORLD"
print("WORD = \"HELLO WORLD\"\nfor i in WORD:\n\tprint(i, end=\"\")")
for i in WORD:
    print(i, end="")
print("\n")    

print("# Print reversed letter.")
print("WORD = \"HELLO WORLD\"\nfor i in range(len(word)-1, -1, -1):\n\tprint(WORD[i], end=\"\")")
for i in range(len(WORD)-1, -1, -1):
    print(WORD[i], end="")
print("\n")

print("# Printing lists.")
NUMBERS = [1,3,2,5]
print("NUMBERS = [1,3,2,5]\nfor i in NUMBER:\n\tprint(i, end=\"\")")
for i in NUMBERS:
    print(i, end="")
print("\n")

print("# For both index and values.")
print("NUMBERS = [1,3,2,5]\nfor i in range(len(NUMBERS)):\n\tprint(f\"NUMBERS[{i}] = {NUMBERS[i]}\")")
for i in range(len(NUMBERS)):
    print(f"NUMBERS[{i}] = {NUMBERS[i]}")

print("# Ignore loop variable. (When you don't care about loop variable.)")
print("for _ in range(5):\n\tprint(\"Hello world!\")")
for _ in range(5):
    print("Hello world!")

print("# Nested loop.")
print("for i in range(2):\n\tfor j in range(2):\n\t\tprint(i, j)")
for i in range(2):
    for j in range(2):
        print(i, j)