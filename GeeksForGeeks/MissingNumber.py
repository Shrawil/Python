def missingNum(arr):
    minimum = min(arr)
    arr = sorted(arr)
    k = minimum
    for i in range(len(arr)):
        print(k, arr[i])
        if k != arr[i]:
            return k
        k += 1
    return k

arr = [2,6,5,1,3]

num = missingNum(arr)
print(num)