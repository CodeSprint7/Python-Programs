"""n=3
  *
 ***
*****
"""
n=int(input("enter n: "))
for i in range(1,n+1):
  print(" "*(n-i)+'*'*(i*2-1))