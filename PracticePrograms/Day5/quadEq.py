def solveQuadratic(equation):
    y = equation
    print(y)
    terms = []
    term = ''
    for ch in y:
        if ch == '-' or ch == '+':
            if term:
                terms.append(term)
            term = ch
        elif ch == ' ':
            continue
        else:
            term += ch
    if term:
        terms.append(term)
    print(terms)
    num1 = int(terms[1][1:len(terms[1])-1])
    num2 = int(terms[2][1])
    factorsFound = False
    for i in range(1, num1+1):
        rem = num1 // i
        if rem * i == num2 and rem + i == num1:
            factorsFound = True
            temp = terms.pop()
            terms.pop()
            terms.append(str(rem)+'x')
            terms.append(str(i)+'x')
            terms.append(temp)
            break
    if not factorsFound:
        print("Equation can't be solved.") 
        exit()
    print(terms)

solveQuadratic('x^2 + 1x - 2')