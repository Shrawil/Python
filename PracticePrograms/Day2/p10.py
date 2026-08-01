# Count Digits, Letters and Symbols
s1 = "python@#123"

upperAlpha = 0
lowerAlpha = 0
symbols = 0
numbers = 0

for i in s1:
    if i.isdigit():
        numbers += 1
    elif i.isalpha():
        if i.isupper():
            upperAlpha += 1
        else:
            lowerAlpha += 1
    else:
        symbols += 1
print(f"There are {upperAlpha} Capital letters {lowerAlpha} small letters {numbers} digits and {symbols} symbols in {s1}.")