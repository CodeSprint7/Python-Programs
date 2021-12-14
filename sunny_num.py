"""N is a sunny number if
N+1 is a perfect square"""
#n=8 ->8+1=9 -->perfect square
#so 8 is a sunny number
import math
n=int(input("Enter a number: "))
x=math.sqrt(n+1)
if(x-math.floor(x)==0):
    print("Is a happy number")
else:
    print("Not a happy number")