"""n=3
*    *
**  **
******
"""
n=int(input("enter n: "))
for i in range(1,n+1):
    print('*'*i+' '*(n*2-(i*2))+'*'*i)