"""
Write a program that reads an array of 5 integers and displays them.

"""

n = 0
numbers = []
while n < 5:
    numbers.append(int(input(f"Input the {n+1}° number: ")))
    n += 1
print(f"The list of numbers are: {numbers}")