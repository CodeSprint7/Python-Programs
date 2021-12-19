"""n=4 
* * * *
 *   *
  * *
   *
  * *
 *   *
* * * *
"""
n=int(input("enter n: "))
for i in range(n-1,-n,-1):
  x=abs(i)
  y=abs(n-x)-1 
  if(x>=n-1 or x==0):
    print(' '*y+'* '*(x+1))
  else:
    print(' '*y+'*'+' '*(x*2-1)+'*')