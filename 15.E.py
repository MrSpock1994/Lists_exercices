"""
Write a program that reads an indefinite number of values, corresponding to grades, ending the data entry when a value
equal to -1 is informed (which should not be stored). After this data entry, do:
a) Show the amount of values that were read;
b) Display all values in the order they were entered, one next to the other;
c) Display all values in reverse order, one below the other;
d) Calculate and display the sum of the values;
e) Calculate and display the average of the values;
f) Calculate and display the amount of values above the calculated average;
g) Calculate and display the number of values below seven;
h) End the program with a message;
"""

grades = []
c = 1
p = 0
b = 0
above_average = []
below_seven = []
while True:
    print("Type -1 if you want to end the program")
    a = float(input(f"Input the {c}º grade: "))
    if a == -1:
        break
    grades.append(a)
    c += 1

# a) Show the amount of values that were read;
print()
print(len(grades))
print()

# b) Display all values in the order they were entered, one next to the other;
print(grades)
print()

# c) Display all values in reverse order, one below the other
for c in range(len(grades)-1, -1, -1):
    print(grades[c])
print()

# d) Calculate and display the sum of the values;
print(sum(grades))
print()

# e) Calculate and display the average of the values;
average = sum(grades) / len(grades)
print(average)
print()

# f) Calculate and display the amount of values above the calculated average;
for c in range(0, len(grades), 1):
    if grades[c] > average:
        above_average.append(grades[c])
        p += 1
print(above_average)
print(p)
print()

# g) Calculate and display the number of values below seven;
for c in range(0, len(grades), 1):
    if grades[c] < 7:
        below_seven.append(grades[c])
        b += 1
print(below_seven)
print(b)
print()

# h) End the program with a message;
print("END OF THE PROGRAM!!")
