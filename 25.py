'''Write a program that can multiply 2 numbers provided by the user
without using the * operator'''

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
product = 0
for i in range(1,num2+1):
    product = product + num1

print("product of two number is: {}".format(product))