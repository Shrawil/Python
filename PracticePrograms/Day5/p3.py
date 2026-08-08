num1 = "123"
num2 = "456"

def getint(num):
    if num == '0': return 0
    elif num == '1': return 1
    elif num == '2': return 2
    elif num == '3': return 3
    elif num == '4': return 4
    elif num == '5': return 5
    elif num == '6': return 6
    elif num == '7': return 7
    elif num == '8': return 8
    elif num == '9': return 9

def getstr(num):
    if num == 0: return '0'
    elif num == 1: return '1'
    elif num == 2: return '2'
    elif num == 3: return '3'
    elif num == 4: return '4'
    elif num == 5: return '5'
    elif num == 6: return '6'
    elif num == 7: return '7'
    elif num == 8: return '8'
    elif num == 9: return '9'

dig1 = 0
dig2 = 0
for i in num1:
    dig1 = dig1 * 10 + getint(i)
for i in num2:
    dig2 = dig2 * 10 + getint(i)
mul = dig1 * dig2
#print(dig1, dig2, mul)
res = ''
while mul != 0:
    digit = mul % 10
    res = getstr(digit) + res
    mul = mul // 10

print(res)