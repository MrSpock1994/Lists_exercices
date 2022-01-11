"""
Write a program that reads 20 integers and stores them in an array. Store the even numbers in the EVEN vector and the
ODD numbers in the odd vector. Print the three vectors.

"""

even = []
odd = []
n = 0

while n < 20:
    a = int(input(f"Input the {n+1}° number: "))
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)
    n += 1

print(even)
print(odd)
