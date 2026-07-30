class Student:
    students = list()

    def __init__(self, name, age, marks):
        self.name = name 
        self.age = age 
        self.marks = {
            'Sub1' : marks[0],
            'Sub2' : marks[1],
            'Sub3' : marks[2],
            'Sub4' : marks[3],
            'Sub5' : marks[4]
        }
        self.students.append([self.name, self.age, self.marks])

s1 = Student('S1', 19, [88, 53, 85, 77, 90]) 
s2 = Student('S2', 19, [70, 74, 66, 48, 99]) 
s3 = Student('S3', 20, [87, 69, 86, 68, 79]) 
s4 = Student('S4', 18, [72, 64, 82, 24, 99]) 
s5 = Student('S5', 19, [98, 34, 36, 38, 89])

'''
n = int(input("How many students record you want to make : "))

for i in range(n):
    name = input("Enter student's name : ")
    age = int(input("Enter student's age : "))
    marks = []
    for i in range(5):
        m = int(input(f"Enter marks for subject {i+1} : "))
        marks.append(m)
    s = Student(name, age, marks)
'''

for student in Student.students:
    print(student)

print("Subject with highest marks - ")
for student in Student.students:
    print(f"{student[0]} - {max(student[2].items(), key=lambda x : x[1])}")

print("Subject with lowest marks - ")
for student in Student.students:
    print(f"{student[0]} - {min(student[2].items(), key=lambda x : x[1])}")

print("Marks in ASC order - ")
for student in Student.students:
    print(f"{student[0]} - {sorted(student[2].items(), key=lambda x : x[1])}")

print("Marks in DESC order - ")
for student in Student.students:
    print(f"{student[0]} - {sorted(student[2].items(), key=lambda x : x[1], reverse=True)}")

print("Subjects student passed in - ")
for student in Student.students:
    total = len(list(filter(lambda x : x[1], student[2].items())))
    passed = len(list(filter(lambda x : x[1] > 50, student[2].items())))
    print(f"{student[0]} - {list(filter(lambda x : x[1] > 50, student[2].items()))} \n[Passed in {passed}]")

print("Subjects student failed in - ")
for student in Student.students:
    total = len(list(filter(lambda x : x[1], student[2].items())))
    failed = len(list(filter(lambda x : x[1] < 50, student[2].items())))
    print(f"{student[0]} - {list(filter(lambda x : x[1] < 50, student[2].items()))} \n[Failed in {failed}]")

print("Average marks of each students - ")
for student in Student.students:
    sum = 0
    for i in list(map(lambda x : x[1], student[2].items())):
        sum += int(i) 
    print(f"{student[0]} - Total : {sum}/500 | Avg : {sum/5}/100")

print("Giving grace marks - ")
for student in Student.students:
    for k, v in student[2].items():
        if student[2][k] + 5 < 100:
            student[2][k] += 5
    print(f"{student[0]} - {list(student[2].items())}")

print("Grades based on total marks - ")
for student in Student.students:
    print(f"\n{student[0]} - ")
    for i in list(map(lambda x : x[1], student[2].items())):
        if i > 90: grade = 'A'
        elif i > 80: grade = 'B'
        elif i > 70: grade = 'C'
        elif i > 60: grade = 'D'
        elif i > 50: grade = 'E'
        else: grade = 'F'
        print(f"Grade  : {grade}", end=" ")

        