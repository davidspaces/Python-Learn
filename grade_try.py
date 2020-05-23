score=float(input("Enter a score between 0.0 and 1.0: "))
try:
    if score >=0.9 and score<=1.0:
        print ("A grade")
    elif score >=0.8 and score <=0.89:
        print ("B grade")
    elif score >=0.7 and score <=0.79:
        print ("C grade")
    elif score >=0.6 and score <=0.69:
        print ("D grade")
    elif score <0.6:
        print ("F grade")
except:
    print ("Enter a number between 0 and 1")
