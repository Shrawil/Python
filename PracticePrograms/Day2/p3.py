# Longest Word

sentence = input("Enter a sentence : ")

words = sentence.split()

largest = words[0]
for word in words:
    if len(word) > len(largest):
        largest = word

print(f"Largest word in \"{sentence}\" is {largest}.")