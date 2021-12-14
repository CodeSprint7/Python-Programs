"""n=5
*
**
* *
*  *
*****
"""
n=int(input("enter n: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print('*'*i)
    else:
        print('*'+' '*(i-2)+'*')