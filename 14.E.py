"""
Using lists write a program that asks five questions to a person about a crime. The questions are:

1- Did you call the victim?
2- were you in the crime scene?
3- Do you live near the victim?
4- Did you owe something to the victim?
5- Have you ever worked with the victim?

In the end the program must issue a classification about the persons participation in the crime.
If you have 2 yes - person is a suspect
if you have 3 or 4 yes - person is an accomplice
if you have 5 yes - person is the murderer
if you have 1 yes - person is innocent

"""

import time
answer_yes = []
n = 0

print("****You should answer the questions bellow with yes or no****\n")

print("First question")
while True:
    a = str(input("Did you call the victim? ")).lower()
    if a not in "yesno" or "":
        print("Invalid answer!")
        break
    if a == "yes":
        answer_yes.append(1)
    print("wait a second....\n")
    time.sleep(1)
    a = str(input("Were you in the crime scene? ")).lower()
    if a not in "yesno" or "":
        print("Invalid answer!")
        break
    if a == "yes":
        answer_yes.append(1)
    print("wait a second....\n")
    time.sleep(1)
    a = str(input("Do you live near the victim? ")).lower()
    if a not in "yesno" or "":
        print("Invalid answer!")
        break
    if a == "yes":
        answer_yes.append(1)
    print("wait a second....\n")
    time.sleep(1)
    a = str(input("Did you owe something to the victim? ")).lower()
    if a not in "yesno" or "":
        print("Invalid answer!")
        break
    if a == "yes":
        answer_yes.append(1)
    print("wait a second....\n")
    time.sleep(1)
    a = str(input("Have you ever worked with the victim? ")).lower()
    if a not in "yesno" or "":
        print("Invalid answer!")
        break
    if a == "yes":
        answer_yes.append(1)
    break

print("Based on the answers provided by the user we have the following result: \n")
if len(answer_yes) == 0 or len(answer_yes) == 1:
    print("Innocent")
if len(answer_yes) == 2:
    print("Suspect")
if len(answer_yes) == 3 or len(answer_yes) == 4:
    print("Accomplice")
if len(answer_yes) == 5:
    print("Murderer")

