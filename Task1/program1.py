# WAP which iterates the integers from 1 to 50. 
# For multiple of three print "Fizz" instead of 
# the number and for the multiples of five print 
# "Buzz". For numbers which are multiples of both 
# three and five print "FizzBuzz".

for i in range(1, 50+1):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output if output else i)
