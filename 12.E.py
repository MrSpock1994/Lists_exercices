"""
The ages and heights of 30 students were recorded. Write a program that determines how many students over 13 are taller
than the average height of these students.

"""
import random

ages = []
heights = []
ages2 = []
p = 0
n = 0

# we can assume that the students age range is 12 to 17 years
# The height range is 150 to 175 cm


while n < 30:
    ages.append(random.randint(12, 17))
    heights.append(random.randint(150, 175))
    n += 1
for c in range(0, len(ages)):
    if ages[c] > 13:
        ages2.append(c)

avg_height = sum(heights) / len(heights)

for c in range(0, len(ages2)):
    if heights[c] > avg_height:
        p += 1

print(p)

