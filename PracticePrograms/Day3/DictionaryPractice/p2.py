# Student Marks

students = ["A", "B"]
marks = [
    [
        ("Sub1", 100),
        ("Sub2", 89),
        ("Sub3", 98),
        ("Sub4", 79),
        ("Sub5", 86)
    ],
    [
        ("Sub1", 76),
        ("Sub2", 85),
        ("Sub3", 72),
        ("Sub4", 84),
        ("Sub5", 80)
    ]
]
dict_student = {}

for i in range(len(students)):
    dict_student[students[i]] = marks[i]

print("Student marks in ascending order : ")
for student in dict_student.items():
    print(f"{student[0]} - {sorted(student[1], key=lambda x : x[1])}")

print("Student marks in descending order : ")
for student in dict_student.items():
    print(f"{student[0]} - {sorted(student[1], key=lambda x : x[1], reverse=True)}")

print("Highest scoring subject of each student - ")
for student in dict_student.items():
    print(f"{student[0]} - {max(student[1], key=lambda x : x[1])}")

print("Lowest scoring subject of each student - ")
for student in dict_student.items():
    print(f"{student[0]} - {min(student[1], key=lambda x : x[1])}")

temp = [["Sub1",0], ["Sub2",0], ["Sub3",0], ["Sub4",0], ["Sub5",0]]
for student in dict_student.items():
    i = 0
    for mark in student[1]:
        temp[i][1] += mark[1]
        i += 1
highest = max(temp, key=lambda x : x[1])
print(f"Highest scoring subject is {highest[0]} with {highest[1]} marks in total.")