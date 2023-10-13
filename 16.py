'''Write a program that will determine weather when the value of
temperature and humidity is provided by the user.
TEMPERATURE(C)   HUMIDITY(%)    WEATHER
>= 30              >=90       Hot and Humid
>= 30            < 90             Hot
<30              >= 90       Cool and Humid
<30               <90              Cool'''


temp = float(input("enter the temp "))
humd = float(input("enter the humidity "))

if (temp>=30) & (humd >= 90):
    print("HOT and HUMID")
elif (temp>=30) & (humd < 90):
    print("HOT")
elif (temp<30) & (humd >= 90):
    print("COLD and HUMID")
elif (temp<30) & (humd <90 ):
    print("COOL")

