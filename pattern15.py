"""n=3
  *
 * *
* * *
* * *
* * *
"""
n=int(input("enter n: "))
for i in range(1,n*2):
    x=' '*(n-i)+'* '*i 
    y='* '*n 
    z=x if(i<=n) else y
    print(z)