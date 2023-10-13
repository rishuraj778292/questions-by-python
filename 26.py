'''Write a program that can find the factorial of a given number provided
by the user.'''

num = int(input("enter the number: "))
fact = 1
if num == 0:
   print("factorial is: 1")
else:
   for i in range(1,num+1):
       fact = fact*i
   print("factorial is: {}".format(fact))
