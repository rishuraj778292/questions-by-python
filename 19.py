'''
Write a program that will take user input of (4 digits number) and
check whether the number is narcissist number or not.
'''
# this programme is for all digit number not only for 4 digit

import math
n = int(input("enter the number "))
# num = n

def digit_count(n):
    counter = 0
    while(n>0):
       remainder1 = n%10
       n = n//10
       counter = counter + 1
    return counter
counter = digit_count(n)

def check_narcissist(x):
    sum = 0
    while x>0:
        remainder2 = x % 10
        sum = sum + pow(remainder2,counter)
        x = x//10
        
    if n == sum:
        print("yes {} is a narcissist number".format(n))
    else:
        print("No {} is not a narcissist number".format(n))


check_narcissist(n)
