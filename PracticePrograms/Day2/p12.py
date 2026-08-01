# Roman to Integer

roman = "IIX"
roman += ' '
def romanVal(ch):
    match ch:
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case _:
            return 0

res = 0
for i in range(len(roman)-1):
    if romanVal(roman[i]) < romanVal(roman[i+1]):
        res -= romanVal(roman[i])
    else:
        res += romanVal(roman[i])
print(roman, res)