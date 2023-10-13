'''Write a program that will swap numbers'''

num1 = int(input("enter the first number A: "))
num2 = int(input("enter the second number B: "))

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print(''' Number after swapping
        A = {}
        B = {}'''.format(num1,num2))