# Student marks analyser python project.

import numpy as np

students = np.array([
    [78, 91, 65, 84],
    [56, 72, 81, 69],
    [92, 88, 76, 95],
    [64, 59, 70, 61],
    [85, 79, 91, 88]
])

names = np.array([
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve"
])

subjects = np.array([
    "C",
    "Python",
    "Maths",
    "DBMS"
])

# Average marks of each student
print(np.mean(students, axis=1))

# Average marks of each subject
print(np.mean(students, axis=0))

# Minimum, Maximum marks in entire array
print(np.min(students), np.max(students))

# Minimum, Maximum marks of each student
print(np.min(students, axis=1), np.max(students, axis=1))

# Minimum, Maximum marks of each subject
print(np.min(students, axis=0), np.max(students, axis=0))

# Name of student with highest/lowest average marks
idx1, idx2 = np.argmax(np.mean(students, axis=1)), np.argmin(np.mean(students,axis=1))
print(f"{names[idx1]} has scored highest average marks and {names[idx2]} has scored lowest average marks.")

# Name of subject with highest/lowest average marks
idx1, idx2 = np.argmax(np.mean(students, axis=0)), np.argmin(np.mean(students,axis=0))
print(f"{subjects[idx1]} is scored with highest average marks and {subjects[idx2]} is scored with lowest average marks.")

# Student above 75 in all subjects
above_75 = np.all(students>75, axis=1)
print(names[above_75])
