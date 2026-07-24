def printIncreasingPower(x):
    for i in range(1, x+1):
        num = i ** 2
        if num > x:
            break
        print (num , end = " ")