# Interval merger

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
newInterval = []
for i in range(len(intervals)-1):
    if intervals[i][1] > intervals[i+1][0]:
        temp = [min(intervals[i]), max(intervals[i+1])]
        newInterval.append(temp)
print(newInterval)