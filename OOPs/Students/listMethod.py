students = [
    ['S1', 19, [
        ['Hindi',84], ['English', 77], ['Maths', 86], ['Science', 76], ['Art', 79]
    ]],
    ['S2', 20, [
        ['Hindi',68], ['English', 86], ['Maths', 96], ['Science', 83], ['Art', 75]
    ]]  
]

print("Marks of each students - ")
for m in students:
    print(f"{m[0]} - {m[2]}")

print("\nMarks of each student in DESC order - ")
for m in students:
    print(sorted(m[2], key=lambda x : x[1], reverse=True))

print("\nMarks of each student in ASC order - ")
for m in students:
    print(sorted(m[2], key=lambda x : x[1]))

print("\nHighest scoring subject of each student - ")
for m in students:
    print(max(m[2], key=lambda x : x[1]))

print("\nLowest scoring subject of each student - ")
for m in students:
    print(min(m[2], key=lambda x : x[1]))

print("\nTotal marks of each student - ")
for m in students:
    total = sum(mark[1] for mark in m[2])
    print(f"{m[0]} - {total}/500")

print("\nAverage marks of each student - ")
for m in students:
    total = sum(mark[1] for mark in m[2])
    print(f"{m[0]} - {total/5}")