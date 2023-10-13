'''Write a program that will take user input of cost price and selling
price and determines whether its a loss or a profit'''

sp = int(input("enter the s.p: "))
cp = int(input("enter the c.p: "))

if sp>cp:
    print("profit")
    print("profit of {}".format(sp-cp))
else:
    print("loss")
    print("loss of {}".format(cp-sp))