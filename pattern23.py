"""left arrow"""
n=int(input("enter no: "))
for i in range(n-1,-n,-1):
  x=abs(i)
  if(x==0):
    print('* '*n)
  elif(x<n-2):
    print('  '*(x)+'*')