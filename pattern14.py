"""n=3
  *
 ***
*****
 ***
  *
"""
n=int(input("enter n: "))
for i in range(n-1,-n,-1):
    x=abs(i)
    y=abs((n-x)*2-1)
    print(' '*x+'*'*y)