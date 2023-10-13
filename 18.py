'''Write a program that will check whether the number is armstrong
number or not.
'''
import math
n = int(input("enter the number "))
num = n
counter = 0

while(n>0):
    remainder1 = n%10
    n = n//10
    counter = counter + 1

def check_armstrong(x):
    sum = 0
    while x>0:
        remainder2 = x % 10
        sum = sum + pow(remainder2,counter)
        x = x//10
        
    if num == sum:
        print("yes {} is a armstrong number".format(num))
    else:
        print("No {} is not a armstrong number".format(num))


check_armstrong(num)


