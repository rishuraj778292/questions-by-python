'''Write a program that can find the factorial of a given number provided
by the user.  by recurssion'''

n= int(input("enter the number: "))
def fact(n):
    if n == 0:
       return 1
    else:
       result = n*fact(n-1)
       return result

factorial = fact(n)
print("factorial is: {}".format(factorial)) 