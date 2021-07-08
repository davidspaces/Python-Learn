#Program to convert temperature from Celsius to Fahrenheit

cel = float(input("Enter the temperature in Celsius:"))
#I'm using float because the temperature can use number with decimal points
fahr= float((cel*1.8)+32)
#We are converting the celsius to Fahrenheit using this formula
print ("It's %.2fF now" %fahr)
#In this case I want to round the float to 2 decimal places, so I used format function
#format(0.2f)- for two decimal places or
#use (%0.2f)- when using string formatting
