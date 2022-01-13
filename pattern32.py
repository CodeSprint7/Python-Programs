#Alphabet 'G' 
n=int(input("enter n: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print(' '+'*'*(n//2))
    elif(i==n//2+1):
        print('* '+'*'*(n//2))
    elif(i>2 and i<=n//2):
        print('*')
    else:
        print('*'+' '*(n//2)+'*')