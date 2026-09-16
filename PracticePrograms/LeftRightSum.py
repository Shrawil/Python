def balancedSums(arr):
    arrLen = len(arr)
    for i in range(arrLen):
        left_sum = 0
        right_sum = 0
        for left in range(i+1):
            left_sum += left
        for right in range(i+1, arrLen+1):
            right_sum += right
        print(left_sum, arr[i], right_sum)

balancedSums([1,2,3,4,5,6])