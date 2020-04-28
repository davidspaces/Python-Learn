#Write a program which repeatedly reads numbers until the user enters "done". 
#Once "done" is entered, print out the total, #count, and average of the numbers. 
#If the user enters anything other than a number, 
#detect their mistake using try and except #and print an error message and skip to the next number.

count =0
sum =0
while True: #This statement denotes the condition that the loop is going to execute until it turns false.
    val=input("Enter a number:")
    if val == 'done':#Checking to see if the string value is set to done.
        break #exits the loop
    try: #To catch the error in case there is a valid number or not.
        fal=float(val)
    except:
        print("Invalid data")
        count=count-1

    count=count+1
    sum=sum+fal

print("The sum is",sum,"The count is",sum,"The average is",sum/count)
