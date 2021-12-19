"""n=3
*    *
**  **
******
**  **
*    * 
"""
n=int(input("enter n: "))
p=n*2 
for i in range(n-1,-n,-1):
    x=n-abs(i)
    print('*'*x+' '*(p-(x*2))+'*'*x)