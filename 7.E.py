"""
Write a program that reads a vector of 5 integers, displays the sum, multiplication and numbers.

"""

numbers = []
n = 0
s = 0
m = 1


while n < 5:
    a = int(input(f"Input the {n+1}° number: "))
    numbers.append(a)
    n += 1
    s += a
    m *= a

print(f"The numbers are {numbers}\n")
print(f"The sum of the numbers: {s}\n")
print(f"The multiplication of the numbers: {m}")