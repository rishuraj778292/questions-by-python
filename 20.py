'''Write a program that will give you the in hand salary after
deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between
5-10 lakh=10%),(11-20lakh=20%),(greater than 20 lakh =30%)(0-1lakh print k).'''

salary = float(input("enter the total yearly salary"))
def in_hand_salary(x):
     if x<500000:
       in_hand = x - (0.1*x + 0.05*x + 0.03*x )
       return in_hand
     elif (500000 <= x <= 1000000):
       in_hand = x - (0.1*x + 0.05*x + 0.03*x + 0.1*x)
       return in_hand
     elif (1100000 <= x <= 2000000):
       in_hand = x - (0.1*x + 0.05*x + 0.03*x + 0.2*x)
       return in_hand
     elif ( x > 2000000):
       in_hand = x - (0.1*x + 0.05*x + 0.03*x + 0.3*x)
       return in_hand
 
net_salary = in_hand_salary(salary)
print("In hand salary is {}".format(net_salary))