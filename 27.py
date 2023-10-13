'''Write a program to print the first 25 odd numbers'''

counter = 0
for i in range(0,100):
    if i%2==0:
        print(i)
        counter = counter +1
   
    if counter == 25:
        break
print("thanks")