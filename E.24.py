"""
Write a program that simulates a roll of the dice. Roll the dice 100 times and store the results in a vector.
Then show how many times each value was achieved

"""

import random

results = []
n = 0
count_results = []
while n < 100:
    results.append(random.randint(1, 6))
    n += 1

c = 1
while c < 7:
    count_results.append(results.count(c))
    c += 1
print(f"The number one appears {count_results[0]} times\n")
print(f"The number two appears {count_results[1]} times\n")
print(f"The number three appears {count_results[2]} times\n")
print(f"The number four appears {count_results[3]} times\n")
print(f"The number five appears {count_results[4]} times\n")
print(f"The number six appears {count_results[5]} times\n")
