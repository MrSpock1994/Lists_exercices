"""
Write a program that reads two vectors with 10 elements each. Generate a third vector of 20 elements,
whose values must be composed of the interleaved elements of the other two vectors.
"""



vector1 = []
vector2 = []
combined_vector = []
n = 0

while n < 10:
    vector1.append(int(input(f"Input the {n+1}° number for vector1: ")))
    combined_vector.append(vector1[n])
    vector2.append(int(input(f"Input the {n+1}° number for vector2: ")))
    combined_vector.append(vector2[n])
    n += 1

print(vector1)
print(vector2)
print(combined_vector)