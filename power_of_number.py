#Power of a number in diff ways
n=int(input("Enter a number: "))
p=int(input("Enter the power: "))
print(n**p)
print(pow(n,p))
res=1
while(p!=0):
    res*=n 
    p-=1 
print(res)
