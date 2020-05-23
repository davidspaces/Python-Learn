#Compute grade function command
def computegrade(score):
    if score >=0.9 and score<=1.0:
        print ("A")
    elif score >=0.8 and score <=0.89:
        print ("B")
    elif score >=0.7 and score <=0.79:
        print("C")
    elif score >=0.6 and score <=0.69:
        print("D")
    elif score <0.6:
        print("F")
        return

scr=input("Enter score:")

try:
    scr=float(scr)
    computegrade(scr)
except:
    print("Bad score")
