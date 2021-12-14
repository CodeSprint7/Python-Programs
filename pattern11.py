"""n=4
****
*  *
*  *
****
"""
n=int(input("enter n: "))
for i in range(1,n+1):
    x=(i==1) or (i==n)
    y='*'+' '*(n-2)+'*'
    s='*'*n if(x) else y
    print(s)