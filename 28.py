'''Write a program to print whether a given number is prime number or
not'''

n = int(input("enter the number: "))

if (n==1) | (n==2):
    print("{} is prime number".format(n))
else:
    for i in range(2,n):
        if n % i == 0:
          print("{} is not prime number".format(n))
          break
        else:
            print("{} is  a prime number".format(n))
            break
    
