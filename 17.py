'''Write a program that will take three digits from the user and add
the square of each digit.'''

import math
a = int(input("enter the first number "))
b = int(input("enter the second number "))
c = int(input("enter the third number "))

sum = pow(a,2)+pow(b,2)+pow(c,2)
print("square sum is {}".format(sum))
