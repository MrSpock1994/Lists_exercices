"""
Write a program that reads a vector A with 10 integers, calculates and displays the sum of the squares of
the elements of the vector

"""

A = []
Asquare = []
for c in range(0, 10):
    A.append(int(input(f"Input the {c+1}° integer: ")))
for c in range(0, 10):
    Asquare.append(((A[c])**2))

print(sum(Asquare))