#User will input (3ages).Find the oldest one

a = int(input("enter the first age "))
b = int(input("enter the second age "))
c = int(input("enter the third age "))
 
if (a>b) & (a>c):
    print("first is oldest one")
elif (b>a) & (b>c):
    print("second is oldest one")
else:
    print("third is oldest one")
