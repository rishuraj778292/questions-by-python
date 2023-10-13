#User will input (2numbers).Write a program to swap the numbers

a = int(input("enter the first number "))
b = int(input("enter the second number "))

# first method -> using third variable

temp = a
a = b
b = temp


print("AFTER THE SWAPPING")
print(a)
print(b)