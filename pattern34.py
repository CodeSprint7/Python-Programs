#Alphabet 'I' 
n=int(input("enter n: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print('*'*n)
    else:
        print(' '*(n//2)+'*')