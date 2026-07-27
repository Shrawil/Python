name = input("Enter your name : ")
args = name.split()
shortName = ''

for i in range(len(args)-1):
    shortName += f"{args[i][0]}."
shortName += args[-1]

print(shortName.title())