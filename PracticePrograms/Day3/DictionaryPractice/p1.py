# Dictionary practice

# Word Counter
text = "apple mango apple banana mango apple"
words = text.split()
word_dict = {}
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
for fruit in word_dict:
    print(f"{fruit} appeared {word_dict[fruit]} times.")