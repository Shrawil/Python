
'''
from functools import reduce
ls = [1,2,3,4,5]

mapls = list(map(lambda x : x * 2, ls))
print(mapls)

filterls = list(filter(lambda x : x % 2 == 0, ls))
print(filterls)

reducels = list(reduce(lambda x, y : x+y, ls))
print(reducels)
'''

'''
for i in range(5):
    print("This is part of loop.")
    if i == 1:
        print("This is part of if inside loop.")    
print("This is not part of loop.")
'''

#print(3*'a')

'''
a = [1,2,3,4,5,6,7,8]
n = 4
for i in range(n):
    a.insert(0, (a.pop()))
print(a)
'''

'''
a = [1, 2, 3]
b = ['a', 'b', 'c']

c = {}

for i in range(len(a)):
    c[a[i]] = b[i]

print(c)
'''


'''
a = 10
num = int(input(">"))
print(a//num)
print("Executed Succesfully.")
'''

'''
a = "(([]))"
ls = []
valid = True

for i in a:
    if i == '(' or i == '[' or i == '{':
        ls.append(i)
    elif i == ')' or i == ']' or i == '}':
        if not ls:
            valid = False
            break
        ch = ls.pop()
        if ch+i not in ['()', '[]', '{}']:
            valid = False
            break
    else:
        valid = False

try:
    ch = ls.pop()
    valid = False
except:
    pass

if valid:
    print("Valid")
else:
    print("Invalid")
'''

'''class Person:
    def __init__(self, username, password):
        self.username = username
        self._password = password
        print("User created!")

class ChangePassword(Person):
    def __init__(self, oldPassword, newPassword):
        if self.password == oldPassword:
            self.password = newPassword
        print("Password changed!")

username = 'Shrawil'
password = 'shrawil123'
a = Person(username, password)
a = ChangePassword(password, 'new123')
'''
'''
class Poly:
    def add(self, a:str, b:str):
        pass
    def add(self, a:int, b:int):
        print(a+b)
    def __str__(self):
        return 'Nothing to show.'
    def __add__(self, a, b):
        return a + b

obj = Poly()
obj.add(1 + 2)
obj.add('A', 'B')
print(obj)
'''

'''
class A:
    def f1(self):
        print("A, f1")
class B:
    def f2(self):
        print(f"B, f2")
class C(B):
    def f3(self):
        print("C, f3")
'''

'''
class A:

class B(A) 

class C(B) # Multi level

class D(A, B) # Multiple

class (D, A, B) # Hybrid
'''
    
'''
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


e01 = Employee('A', 25, 30000)
print(e01)
'''

'''
ls = [1,2,3,4,5]
ls.max()
'''

'''class Student:
    def show(self):
        print(self.name, self.age)

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student()
'''
'''
class Vehicle:
    def add(self):
        print("Add.")
    def mul(self):
        print("Mul.")
    def __init__(self, no_of_tires):
        print("__init__")
    
v1 = Vehicle(4)
v2 = Vehicle(3)
'''

'''
day = int(input("Enter a number : "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Their are 7 days in a week idiot.")
'''

'''
ch = {}

s = "ABBCCCDDD"

for i in s:
    ch[i] = s.count(i)

print(ch)

for i in ch:
    if ch[i] == (min(ch.values())):
        print(i)
'''
# print(sorted([4,3,2,1]))

'''
ls = [7,5,8,3,4,31,54,5]
ls.reverse()
print(ls)
print(list(reversed(ls)))
'''

'''for i in range(5):
    for j in range(4):
        print(' ', end='')
    for j in range(i+1):
        print(chr(j+65), end=' ')
    print()
'''
'''
a = [2,3,4,5,6,7,8,9]
target = 10`

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i]+a[j] == target:
            print(f"{a[i]}, {a[j]}")

'''

'''
a = [1,0,3,0,4,5,4,3,0,0,1,2]
res = [] 

for i in a:
    if i != 0:
        res.append(i)

res.extend([0]*(len(a)-len(res)))
print(res)
'''

'''
for i in range(len(a)):
    if i == 0:
        a.append(a.pop(a[i]))
print(a)
'''

'''
a = 'aabbccc'
b = ''
count = 1

for i in range(0, len(a)-1):
    if a[i] == a[i+1]:
        count += 1
    else:
        b += a[i]
        b += str(count)
        count = 1
b += a[-1]+str(count)
'''

'''
for i in range(len(a)):
    count = 0
    b += a[i]
    for j in range(i, len(a)):
        if b[i] != a[j]:
            b += str(count)
            b += a[j]
        else:
            count += 1
'''
    
'''
string = 'a2b3c2'
for i in range(0, len(string), 2):
    print(string[i]*int(string[i+1]), end='')
'''


'''
for i in range(0, len(string), 2):
    for j in range(int(string[i+1])):
        print(string[i], end='')

'''

'''
str1 = 'aabbcc'
str2 = 'ccaaab'

n1 = sorted(str1)
n2 = sorted(str2)

if (n1 == n2):
    print(f"{str1} is anagram!")
else:
    print(f"{str1} is not anagram!")
'''

'''
s = 'tHIS@iS@mY@cOUNTRY'

ls = s.split('@')
new = ''
for i in ls:
    new += i 
    new += ' '

print(new.title())
# s = s.replace('@', '.')
'''

'''
students = [
    ['S1', 19, [
        ['Hindi',84], ['English', 77], ['Maths', 86], ['Science', 76], ['Art', 79]
    ]],
    ['S2', 20, [
        ['Hindi',68], ['English', 86], ['Maths', 96], ['Science', 83], ['Art', 75]
    ]]
]

for i in students:
    print(f"{i[0]} - {sorted(i[2], key=lambda x : x[1], reverse=True)}")

for i in students:
    print(f"{i[0]} - {sorted(i[2], key=lambda x : x[1], reverse=False)}")

for i in students:
    print(max(i[2], key=lambda x : x[1]))

for i in students:
    print(min(i[2], key=lambda x : x[1]))

for i in students:
    print(min(i[2], key=lambda x : x[1]))

for i in students:
    print(sum(marks[1] for marks in i[2]))

for i in students:
    print(sum(marks[1] for marks in i[2])/5)
'''

'''
a = [5,4,3,8,7,4,9,2,7,2,6]

b = []

for i in range(0, len(a)-1, 2):
    b.append(a[i+1])
    b.append(a[i])

if len(b) < len(a):
    b.append(a[-1])

print(a)
print(b)
'''

'''
def AC(f):
    def wrapper():
        print("A")
        f()
        print("C")
    return wrapper

@greet 
def B():
    print("B")

B()
'''

'''
def s(num):
    if num >= 5:
        return 5
    return num + s(num+1)

print(s(2))
'''

'''
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact(5))
'''

'''
def isAllEven(num):
    for i in str(num):
        if int(i) % 2 != 0:
            return False
    return True 

for i in range(200, 401):
    if isAllEven(i):
        print(i)
'''

'''
def x():
    return 1, 2

a, b = x()
print(a,b)
'''

'''
import math

print(math.factorial(5))
print(math.sqrt(4))
print(math.cbrt(9))
print(math.pow(2,3))
print(math.pi)
print(math.sin(0))
print(math.cos(0))
print(math.tan(45))
'''
'''
def largest(ls):
    l = ls[0]
    for i in ls:
        if i > l:
            l = i 
    return l

l = largest([1,2,3,4,5])
print(largest(l))
'''

'''
def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)

fact = factorial(5)
print(fact)
'''

'''
a = [3,4,6,7,8,3,1]
max = a[0]
min = a[0]

for i in a:
    if max < i:
        max = i
    elif max > i:
        min = i

print(max, min)
'''

'''
a = {'name':'xyz', 'marks':{'Maths':40, 'Hindi':80}}

print(a['marks']['Maths'])
'''

'''
# WAP to reverse a name
name = 'SHRAWIL'
rev = ''

# name = name.reversed()
# print(name[::-1])

for i in range(len(name)-1, -1, -1):
    rev += name[i]

print(rev)
'''

'''
a = {
    'a':1,
    'b':2
}

print(a)
print(a.pop('a'))
print(a)
'''

# User defined dictionary.
'''
length = int(input("Enter length of dictionary : "))
d = dict()

for i in range(length):
    key = input("Enter a key : ")
    value = eval(input(f"Enter value for {key} : "))

    d[key] = value

print(d)
'''

'''
a = [3,4,5,3,4,7,8,6,4,5]

count_dict = {}

for i in a:
    count_dict[i] = a.count(i)

print(count_dict)
'''

'''
visited = list()
for i in a:
    if i not in visited:
        print(i, ' count = ', a.count(i))
        visited.append(i)
'''

'''
d = {
    'name':'xyz',
    'age':19,
}

print(d.pop('name'))
print(d)
d['name'] = 'abc'

print(d)
'''

'''
a = [2,3,4,5,6,7]

for idx, val in enumerate(a):
    print(idx, val)'''

'''

# Dictionary - Stores value in key value pairs.

d = {
    'name':'xyz',
    'age':19,
}

print(d, type(d))
print('d.key() : ', d.keys())
print('d.values() : ', d.values())
print('d.items() : ', d.items())

d['name'] = 'abc'
d['city'] = 'Sitapur'

print(f"d.get('name') : {d.get('name')}")
'''
'''length = int(input("Enter number of items in list : "))
a = []
for i in range(length):
    num = int(input(f"Item #{i+1} : "))
    a.append(num)

a = [1,2,3,4,5,6,7]

for i in range(len(a)-3):
    if a[i] == a[i+1]-1 and a[i] == a[i+2]-2 and a[i] == a[i+3]-3:
        print(a[i], a[i+1], a[i+2], a[i+3])
'''
 

'''a = (1,2,3,4,5)

print(a.count(1))
print(a.index(1))'''

'''from myLib.easyInput import get_and_check

age = get_and_check('Age : ', int)
print(age)'''

'''
a = [1,2,3,4,4,5,5,6]
a = set(a)
print(a)
'''

'''
a = (1,2,3,4,[1,2,3],)
print(a)
a[4][0] = -1
print(a)
'''

'''
name = input("Enter your name : ")
args = name.split()
shortName = ''

for i in range(len(args)-1):
    shortName += f"{args[i][0]}."
shortName += args[-1]

print(shortName.title())
'''

'''
a = [i for i in range(1,10)]
print(a)

c = [i**2 for i in a if i % 2 == 0]
print(c)

d = [i for i in a]
print(d)

'''

'''
ls = [1,6,2,2,5,1,8]

# Sort the list 
ls = sorted(ls)

ls2 = [ls[0]]
for item in ls:
    if item != ls2[-1]:
        ls2.append(item)

print(ls, ls2)
'''

'''
length = int(input("Enter a length : "))
names = list()
for i in range(length):
    names.append(input("Enter a name : "))
for name in names:
    if name[0] == name[len(name)-1]:
        print(f"{name} Start = End")
'''

'''

name = input("Enter your name : ")
name = name.lower()

if name[0] == name[len(name)-1]:
    print("Name starts and ends with same character.")
else:
    print("Name does not start and end with same character.")
'''

'''
items = input("Enter numbers for list [Seperated by space ]: ")
temp = items.split(',')
ls = list()
for item in temp:
    if item.isnumeric():
        ls.append(int(item))
    elif item.isalpha() or item.isalnum():
        ls.append(item)
print(ls)
'''

'''
a = [1,2,4,5]
# Get max value in a
print(max(a))
# Get min value in a 
print(min(a))
# Print all values in a 
print(a)
# Append a value in a 
a.append(6) # Add at last
print(a)
# Append at specific index.
#    index, value
a.insert(2, 3)
print(a)
# Removes and return last value from list
print('Poped = ', a.pop())
print(a)
# Remove a value
a.remove(1)
# Sorts a list
a.sort()
print(a)
a.extend([6,7,8,9])
print(a)
'''

'''
a = [1,2,3,4,5,6,7]
even = list()
for i in a:
    if i % 2 == 0:
       even.append(i)
print(even) 
'''

#a = eval(input('>'))

#print(type(a))

'''
a = 10 
print(a is 10) # Will run with warning.
'''

'''
a = 6 
b = 10

a = (a + b)
b = (a - b)
a = (a - b)

print(a, b)
'''

'''
# String functions 

a = 'XYZ abc'

print(len(a))
print(a.swapcase())
print(a.split())
print(a.title())
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.index('X'))
print(a.find('a'))
print(a.count('Y'))
# print(a[start:stop:step])
print(a[1:len(a):2])
print('SITAPUR'[7:2:-2])
'''

'''
# Ternary operator
print("If is true" if condition else "If is false")
'''

'''
num = int(input("Enter a number : "))
copy = num
rev = 0

while copy > 0:
    # Take last digit of copy
    digit = copy % 10
    rev = (rev * 10) + digit
    copy = copy // 10
 
print(f"{num} reversed = {rev}")

if num == rev:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
'''

'''
a = int(input("Enter a number to find factorial of : "))

# We assume the number is prime by default
pole = True

# Start from 2 and go upto a.
for i in range(2, a):
    # If a's remainder become 0 it mean the number is not a prime number.
    if a % i == 0:
        pole = False
        break

if pole:
    print(f"{a} is a prime number.")
else:
    print(f"{a} is not a prime number.")
'''
    

'''
def main():
    a = int(input("Enter a number to find factorial of : "))
    num2 = a
    fact = 1
    while a > 1:
        print(f"{a} x ", end="")
        fact *= a
        a = a - 1
    print(f"1.\nFactorial of {a} is {fact}!")

if __name__ == '__main__':
    main()
'''


"""
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print(f"{a} is greater than {b}." if a > b else f"{b} is greater that {a}.")

a = int(input("Enter first number : "))

print(f"{a} is even." if a % 2 == 0 else f"{a} is odd.")
"""

"""
start = int(input("Enter value for start : "))
end = int(input("Enter value for end : "))
step = int(input("Enter value for step : "))

while start <= end:
    print(start, end=" ")
    start += step
"""

"""
a = int(input("Enter a number : "))

if a % 3 == 0: 
    print('FIZZ', end="")
if a % 5 == 0:
    print('BUZZ', end="")
"""