"""n=4 
* 
 * * 
  *  *
   *   *
  *  *
 * *
*
"""
n=int(input("enter n: "))
for i in range(n-1,-n,-1):
  x=abs(i)
  if(x>=n-1):
    print(' '*abs(x-n+1)+'*')
  else:
    print(' '*abs(x-n+1)+'*'+' '*(n-x-1)+'*')