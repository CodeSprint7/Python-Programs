#sum of the digits of a number
n=int(input("Enter a number: "))
sum=0
while(n>0):
    sum+=(n%10)
    n//=10 
print("sum of the digits is:",sum)