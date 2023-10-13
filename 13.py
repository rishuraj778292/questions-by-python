'''Write a program that will tell whether the given number is divisible
by 3 & 6.'''

n = int(input("enter the number "))
num2 = n
sum = 0
while(n>0):
  remainder = n % 10
  sum = sum + remainder
  n = n // 10
  
if (sum%3==0)&(num2 %2==0):
  print("the number {} is divisible by 6 and 3".format(num2))
elif (sum % 3 == 0 ):
  print("the number {} is divisible by  3".format(num2))
else:
  print("the number {} is not divisible by 3 and 6".format(num2))