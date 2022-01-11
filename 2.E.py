"""
Write a program that reads an array of 10 real numbers and displays them in reverse order.

"""

n = 0
numbers = []
numbers_reversed = []
while n < 10:
    numbers.append(int(input(f"Input the {n+1}° number: ")))
    n += 1

for c in range(9, -1, -1):
    numbers_reversed.append(numbers[c])

print(f"Normal array {numbers}")
print(f"Array in reverse order {numbers_reversed}")
