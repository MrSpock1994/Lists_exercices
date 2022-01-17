"""
Make a program that takes the average temperature for each month of the year and stores them in a list. After that,
calculate a average temperatures plus all temperatures above the annual average, and yearly in which month they
(show the month in full: 1 – January, 2 – February, . . . ).

"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November'
         , 'December']
average_month = []
above_average = []
n = 0
x = 0
while n < 12:
    average_month.append(float(input(f"Please input the average temperature for {months[n]}: ")))
    n +=1

averagetemp = sum(average_month)/ len(average_month)

for c in range(0, 12):
    if average_month[c] > averagetemp:
        above_average.append(c)

print(f"The average annual temperature was {round(averagetemp, 2)}. \n")
print(f"All months bellow had an average temperature above annual: \n")

while x < len(above_average):
    print(f"{months[above_average[x]]}")
    x += 1