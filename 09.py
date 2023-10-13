''' Write a program that take a user inputr of three angles and will
find out whether it can form a triangle or not.'''

a = int(input("enter the first angle "))
b = int(input("enter the second angle "))
c = int(input("enter the third angle "))

if a+b+c == 180:
    print("yes it form a triangle")
else:
    print("no it not form a traingle")