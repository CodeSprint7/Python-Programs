"""If the sum and product of its 
digits are equal -->spy number"""
#n=132 sum=1+3+2=6 prod=1*3*2=6 
n=int(input("Enter a number: "))
sum,prod=0,1 
while(n):
    x=n%10 
    sum+=x 
    prod*=x 
    n//=10 
if(sum==prod):
    print("Is a spy number")
else:
    print("Is not a spy number")