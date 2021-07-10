#Compute pay using functions

def computepay(hours,rate):
    if hours > 40:
        pay = ((hours-40)*(rate*1.5))+(40*rate)
    else:
        pay=(hours*rate)
    return pay

hr=float(input("Enter the number of hours:"))
rt=float(input("Enter the pay rate:"))
pay=computepay(hr,rt)

print ("Your pay is:$",pay)
