nums = [3, 2, 5, 1, 7, 4, 6]

ls = []
sum = 0
for num in nums:
    sum += num
    ls.append(sum)

queries = [   
    [1, 4],
    [2, 5],
    [0, 3],
    [3, 6],
    ]

for q in queries:
    if min(q) > 0:
        res = ls[max(q)] - ls[min(q)-1]
    else:
        res = ls[max(q)]
    print(res)