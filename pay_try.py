hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
try:
    if hours <=40:
        pay = (hours*rate)
        print ("Your pay is $",pay)
    else:
        pay = ((hours-40)*(rate*1.5))+(40*rate)
        print (pay)
except:
    print ("Error, enter a numeric value")
        
