"""

Write a program that asks for the age and height of 5 people, store each information in its respective vector.
Print age and height in reverse order of read order.

"""

age = []
height = []
age_reversed = []
height_reversed = []
n = 0

while n < 5:
    age.append(int(input(f"Input the age for the {n+1}° person: ")))
    height.append(float(input(f"Input the height in cm for the {n+1}° person: ")))
    n += 1

for c in range(4, -1, -1):
    age_reversed.append(age[c])
    height_reversed.append(height[c])

print(age)
print(age_reversed)
print(height)
print(height_reversed)


