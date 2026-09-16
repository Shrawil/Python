def hourglassSum(arr):
    # Write your code here
    print(arr)
    row = 0
    sum = arr[0]
    highest = sum
    while row < 24:
        for i in range(row, row+4):
            try:
                print(f"{arr[i]}\t{arr[i+1]}\t{arr[i+2]}\n\t{arr[i+7]}\n{arr[i+12]}\t{arr[i+13]}\t{arr[i+14]}")
            except:
                print("Program stopped at index : ", i)
            sum = arr[i] + arr[i+1] + arr[i+2] + arr[i+7] + arr[i+12] + arr[i+13] + arr[i+14]
        if highest < sum:
            highest = sum
        row += 6
    return highest

print(hourglassSum([
    1,1,1,0,0,0,
    0,1,0,0,0,0,
    1,1,1,0,0,0,
    0,0,0,0,0,0,
    0,0,0,0,0,0,
    0,0,0,0,0,0,
]))