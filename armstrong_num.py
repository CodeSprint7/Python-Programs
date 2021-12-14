"""Armstrong number --> sum of the
cubes of the each digit of a num"""
n=int(input("Enter a number: "))
temp,res=n,0 
while(n>0):
    t=n%10
    res+=(t**3)
    n=n//10 
if(res==temp):
    print("Armstrong number")
else:
    print("Not a armstrong number")