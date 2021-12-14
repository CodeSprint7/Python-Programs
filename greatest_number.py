#Greatest among three numbers
#1st approach
a,b,c=map(int,input().split())
print(max(max(a,b),c))
#2nd approach
if(a>=b and a>=c):
    print(a)
elif(b>=a and b>=c):
    print(b)
else:
    print(c)