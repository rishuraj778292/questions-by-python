'''
Write a menu driven program - 1.cm to ft 2.kl to miles 3.usd to inr
4.exit
'''
print("-----------choose one----------")
print("1. cm to ft")
print("2. kl to miles")
print("3. usd to inr")
print("4. exit")
print("-------------------------------")

n = int(input("enter your choice "))

def cm_ft():
    print("you chosse cm to fit")
def kl_miles():
   print("you chosse kl to miles")
def usd_inr():
    print("you chosse usd to inr")


if n == 1:
    cm_ft()
elif n==2:
    kl_miles()
elif n==3:
    usd_inr()
elif n==4:
    print('''thanks!
          Good Byee!''')
else:
    print("sorry! invalid input , re-choose")
        





