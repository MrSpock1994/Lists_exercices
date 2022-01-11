"""
Write a Program that reads 4 grades, shows the grades and the average on the screen.

"""

grades = []
n = 0

while n < 4:
    grades.append(float(input(f"Input the {n+1}° grade: ")))
    n += 1
print(f"Your grades are: {grades}")
print(f"Your average grade is {sum(grades)/len(grades)}")