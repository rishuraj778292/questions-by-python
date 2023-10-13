'''Write a program to find the simple interest when the value of
principle,rate of interest and time period is given.'''

p = float(input("principle => "))
r_o_i = float(input("rate of interest => "))
t_p = float(input("time period => "))

s_i = (p*r_o_i*t_p)/100
print(format(s_i ,'.2f'))