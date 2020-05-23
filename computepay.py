#Compute Pay function for pay rate

def computepay(hours,rate):
    if hours >40:
        pay=((hours-40)*(rate*1.5))+(40*rate)
    else:
        pay=(hours*rate)
    return pay

fh=float(input("Enter the number of hours:"))
fr=float(input("Enter the rate:"))
pay=computepay(fh,fr)

print ("Your pay is:$",pay)
