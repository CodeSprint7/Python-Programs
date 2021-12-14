"""Neon number is a number where the
sum of the digits of square of the
number is equal to the num"""
#num=9 9*9=81 8+1=9--> 9==9-->neon num
n=int(input("Enter a number: "))
sum,s=0,n*n 
while(s>0):
    sum+=s%10 
    s//=10 
if(sum==n):
    print("Is a neon number")
else:
    print("Not a neon number")