# Write a program that will tell whether the given year is a leap year or not.

year = int(input("enter the year "))

if year%100 == 0:
    if year%400 == 0:
        print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))
else:
    if year % 4 == 0:
        print("{} is a leap year".format(year))
    else :
        print("{} is not a leap year".format(year))

