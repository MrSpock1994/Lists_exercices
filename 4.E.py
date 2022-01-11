"""

Write a program that reads a 10-character vector, and tells you how many consonants were read. print the consonants

"""


word = str(input("Input the word: "))
list_vogals = ['a', 'e', 'i', 'o', 'u']
consonants = []

for c in range(0, len(word)):
    if word[c] not in list_vogals:
        consonants.append(word[c])

print(f"We have {len(consonants)} consonant in the word {word}\n")
print(consonants)

