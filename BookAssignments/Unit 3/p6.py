n = input("Enter comma-seperated numbers : ")
ls = n.split(',')
ls = list(map(lambda x : x.strip(), ls))
print(sorted(ls))