"""Strong number --> sum of the
factorials of the digits"""
import math
n=int(input("Enter a number: "))
temp,res=n,0 
while(n>0):
    res+=math.factorial(n%10)
    n//=10 
if(res==temp):
    print("Strong number")
else:
    print("Is not a strong number")