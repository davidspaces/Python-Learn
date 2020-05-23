#Grading
try:
    score=float(input("Enter your score between 0.0 and 1.0:"))
    if score >=0.9 and score <=1.0:
        print ("A grade")
    elif score >=0.8 and score <0.9:
        print ("B grade")
    elif score >=0.7 and score <0.8:
        print ("C grade")
    elif score >=0.6 and score<0.7:
        print ("D grade")
    elif score<0.6:
        print ("Don't you have any shame for failing")
    elif score >1.0:
        print ("You can't score more than 1")
except:
    print ("Enter a number you moron")
