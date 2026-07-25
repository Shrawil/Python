length = int(input("Enter a length : "))
names = list()
for i in range(length):
    names.append(input("Enter a name : "))
for name in names:
    if name[0] == name[len(name)-1]:
        print(f"{name} Start = End")