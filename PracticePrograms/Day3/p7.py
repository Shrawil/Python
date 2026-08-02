# Custom groupby()

ls = [
    ("A", 1),
    ("B", 2),
    ("D", 2),
    ("C", 1),
]

group = {}

for i in ls:
    if i[1] not in group:
        group[i[1]] = list(i[0])
    else:
        temp = group.get(i[1])
        temp.append(i[0])
        group[i[1]] = temp
print(group)
