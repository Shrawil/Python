a = {
    'a':1,
    'b':2
}

print(a)
print(a.pop('a'))
print(a)

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