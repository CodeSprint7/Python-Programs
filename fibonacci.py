#Fibonacci series
n=int(input("Enter number of terms: "))
a,b=0,1 
if(n==1):
    print(a)
else:
    print(a,b,end=" ")
    for i in range(n-2):
        c=a+b 
        a,b=b,c
        print(c,end=" ")