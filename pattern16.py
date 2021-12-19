"""n=3 
* * *
 * * 
  *
 * *
* * * 
"""
n=int(input("enter n: "))
for i in range(n-1,-n,-1):
    x=abs(i)
    print(' '*(abs(n-x))+'* '*(x+1))