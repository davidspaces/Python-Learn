#Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
max=None
min=None
while True:
    digit=input("Enter a number:")
    if digit == 'done':
        break
    try:
        fgit=float(digit)
    except:
        print("Enter a numeric value")
        continue
    if max is None:
        max = fgit #Assigning the numeric value
    if min is None:
        min = fgit #Assigning the numeric value
    if fgit > max:
        max = fgit
    elif fgit < min:
        min = fgit

print("Max is",max)
print("Min is",min)
