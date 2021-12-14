#To find super digit of a number
"""super digit is a sum of all
digits repeatedly until the
sum is a single digit number"""
#n=87 -->8+7=15 -->1+5=6 super dig
n=int(input("Enter a number: "))
sum=0 
while(n>0 or sum>9):
    if(n<=0):
        n=sum 
        sum=0 
    sum+=n%10 
    n//=10 
print(sum)