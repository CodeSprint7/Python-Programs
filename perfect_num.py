n=int(input())
m=int(input())
count=0
for j in range(n,m+1):
    sum=1
    for i in range(2,j):
        sum=sum+i if(j%i==0) else sum
    if(sum==j):
        count+=1 
print(count)
