# Longest Consecutive Sequence

nums1 = [8,7,6,5,6,7,8,1,2,3,6]

def seq(idx, ls):
    temp = []
    num = ls[idx]
    count = 0
    for i in range(idx, len(ls)):
        if num+count == ls[i]:
            temp.append(ls[i])
            count += 1
        else: 
            break
    return temp

best = []
for i in range(len(nums1)):
    # Send currect index and list
    cur = seq(i, nums1)

    if len(cur) > len(best):
        best = cur 

print(best)