"""n=3 
  *
 * *
*   *
 * * 
  *
"""
n=int(input("enter n: "))
for i in range(n-1,-n,-1):
    x=abs(i)
    if(x>=n-1):
        print(' '*x+'*')
    else:
        print(' '*x+'*'+' '*(n*2-x*2-3)+'*')