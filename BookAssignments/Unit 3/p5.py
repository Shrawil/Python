# Take input as comma-seperated numbers eg. 1,2,3,4,5
# Convert them into list and tuple

n = input("Enter comma-seperated numbers : ")
n_list = n.split(',')

l = list()
print(n_list)
for item in n_list:
    try:
        l.append(eval(item))
    except:
        continue

t = tuple(l)

print(l, t)