def hourglassSum(arr):
    # Write your code here
    sum = 0
    highest = -float('inf')
    for r in range(4):
        for c in range(len(arr)-2):
            #print(f"{arr[r][c]}\t{arr[r][c+1]}\t{arr[r][c+2]}\n\t{arr[r+1][c+1]}\n{arr[r+2][c]}\t{arr[r+2][c+1]}\t{arr[r+2][c+2]}")
            sum = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
            if highest < sum:
                highest = sum
    return highest

print(hourglassSum(
    [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
))