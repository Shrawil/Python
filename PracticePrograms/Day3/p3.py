# Validate Parentheses

s = "([]))))))))))"

check = []
isValid = True

for i in s:
    if i == "(" or i == "[" or i == "{":
        check.append(i)
    elif i == ")" or i == "]" or i == "}":
        try:
            temp = check.pop()
        except IndexError:
            isValid = False
            break
        if temp+i not in ("()", "[]", "{}"):
            isValid = False
    else:
        isValid = False
        break

if isValid and str(check) == "[]":
    print(f"{s} is valid!")
else:
    print(f"{s} is not valid!")