#Alphabet 'P'
n=int(input("enter n: "))
for i in range(0,n+1):
    if(i==0 or i==n//2):
        print('*'*(n//2))
    elif(i<n//2):
        print('*'+' '*(n//2-1)+'*')
    else:
        print('*')