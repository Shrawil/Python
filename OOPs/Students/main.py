class Student:
    students = list()
    def __init__(self, name: str, age: int, m: list):
        self.name = name
        self.age = age
        self.marks = {
            'Hindi':m[0],
            'English':m[1],
            'Maths':m[2],
            'Science':m[3],
            'Art':m[4]
        }
        self.students.append([self.name, self.age, self.marks])
        

    def __str__(self):
        return f'{self.name} | {self.age} | {self.marks}'

s1 = Student('S1', 19, [88, 53, 85, 77, 90])
s2 = Student('S2', 19, [70, 74, 66, 48, 99])
s3 = Student('S3', 20, [87, 69, 86, 68, 79])
s4 = Student('S4', 18, [72, 64, 82, 24, 99])
s5 = Student('S5', 19, [98, 34, 36, 38, 89])

print("Marks in DESC order - ")
for student in Student.students:
    print(f"{student[0]} - {sorted(student[2].items(), key=lambda x : x[1], reverse=True)}")

print("Marks in ASC order - ")
for student in Student.students:
    print(f"{student[0]} - {sorted(student[2].items(), key=lambda x : x[1])}")

print("Highest Marking Subject - ")
for student in Student.students:
    print(f"{student[0]} - {max(student[2].items(), key=lambda x : x[1])}")

print("Lower Scoring Subject - ")
for student in Student.students:
    print(f"{student[0]} - {min(student[2].items(), key=lambda x : x[1])}")
