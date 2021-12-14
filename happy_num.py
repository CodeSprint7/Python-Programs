"""happy number-->if it yields 1 
when replaced by the sum of 
squares of its digits repeatedly"""
n=int(input("Enter a number: "))
sum=0 
while(n>0 or sum>9):
    if(n<=0):
        n=sum 
        sum=0 
    sum+=(n%10)**2 
    n//=10 
if(sum==1):
    print(1)
elif(sum==4):
    print(0)