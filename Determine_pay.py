try: #To catch any misidentified characters
    hours = float(input("enter the number of hours: "))
    rate = float(input("enter the rate:"))
    #Adding conditional statement to check for different conditions
    if hours <=40:
        grosspay = hours*rate
        print ("The pay is:",grosspay)
    else:
        grosspay=float(((hours-40)*(rate*1.5))+(40*rate))
        print ("The pay is:",grosspay)
except:
    print("Enter a valid number")
