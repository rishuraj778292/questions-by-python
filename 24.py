'''Write a program to find the sum of first n numbers, where n will be
provided by the user. Eg if the user provides n=10 the output should be
55'''

n = int(input("enter the value of n: "))
result = (n*n+n)/2
print("sum upto {} is: {}".format(n,result))