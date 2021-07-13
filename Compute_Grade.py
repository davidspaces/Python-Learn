#Using functions to check the grade. Creating a computegrade function to use for the grade.

def computegrade(score):
    if score >=0.9 and score<=1.0:
      print ("A Grade")
    elif score >=0.8 and score<=0.89:
      print ("B Grade")
    elif score >=0.7 and score <=0.79:
      print ("C Grade")
    elif score >=0.6 and score <=0.69:
      print ("D Grade")
    elif score <0.6:
      print ("F Grade")
      return

scr=input("Enter score to know your grade:")
try:
    scr=float(scr)
    computegrade(scr)
except:
    print("Bad score")
