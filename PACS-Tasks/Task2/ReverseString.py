# Reverse every word.  (Python is fun   Output nohtyP si nuf)

sentence = input("Enter a sentence : ")

words = sentence.split()

for word in words:
    print(word[::-1], end=' ')