#Pay
try:
    hours = float(input("Enter the number of hours: "))
    rate = float(input("Enter the pay rate per hour: "))

    if hours >=40:
        salary=((hours-40)*(rate*1.5))+(hours*rate)
    else:
        salary=(hours*rate)

    print ("Your weekly salary is %d"%(salary))
except:
    print ("enter a numeric value")
