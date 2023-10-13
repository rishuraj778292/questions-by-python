import math

p = int(input("x axis of 1st cord. : "))
q = int(input("y axis of 1st cord. : "))
x = int(input("x axis of 1st cord. : "))
y = int(input("y axis of 1st cord. : "))

temp = pow((p-x),2) + pow((q-y),2)
distance = math.sqrt(temp)
print(format(distance , '.2f' ))