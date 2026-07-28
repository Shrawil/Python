def frequencyStr():
    word = input("Enter a word : ")
    d = {}

    for a in word:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1

    return d 

if __name__ == '__main__':
    items = frequencyStr()
    for item in items:
        print(f'{item} - {items.get(item)}')