#Write a python program to find the sum of all even numbers from 0 to 10
num=0
sum=0
while num <10:
  num=int(num+1)
  if (num%int(2))==0:
     sum = sum+num
print (sum)
