'''Print all the armstrong numbers in the range of 100 to 1000'''
import math
counter =0
sum =0
for i in range (100,1000):
    n = i
    m = i
    while(n>0):
        counter = counter +1
        n = n // 10
    while m>0:
        remainder = m%10
        sum = sum + pow(remainder,counter)
        m = m//10
    if sum == i:
        print(i)
    counter =0
    sum =0
    


    
    