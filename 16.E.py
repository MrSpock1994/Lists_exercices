"""
Write a function called has_duplicates that takes a list and returns True if there is any element that appears more
than once. It must not modify the original list.

"""


def has_duplicates(list):
    dupl = []
    for c in range(0, len(list)):
        list.count(list[c])
        if list.count(list[c]) > 1:
            dupl.append(list[c])
    if len(dupl) > 0:
        print("The list has duplicated elements.")
    else:
        print("The list does not have duplicated elements.")


numbers = [1, 2, 3, 4, 5, 5]
has_duplicates(numbers)