"""
Write a program that asks for the four grades of 10 students, calculate and store the average of each student in a vector,
print the number of students with an average greater than or equal to 7.0.

"""

grades = []
average_grade = []
n = 0
p = 0

while n < 10:
    for c in range(0, 4):
        grades.append(float(input(f"Input the {c+1}° grade of the {n+1}° student: ")))
    average_grade.append(sum(grades)/len(grades))
    grades.clear()
    n += 1

for c in range(0, len(average_grade)):
    if average_grade[c] >= 7:
        p += 1

print(f"{p} students has an average grade greater or equal to 7.0.")
