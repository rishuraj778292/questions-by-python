'''Write a program that will reverse a four digit number.
Also it checks whether the reverse is true.'''

n = int(input("enter a number "))
rev_number = 0
while n>0:
     remainder = n % 10
     rev_number = rev_number*10 + remainder
     n = n // 10
     
print("the revse number is {}".format(rev_number))



