#Alphabet 'A'
n=int(input("enter n: "))
for i in range(1,n+1):
    x=n-i 
    if(i==1):
        print(' '*x+'*')
    elif(i==n//2+1):
        print(' '*x+'*'*n)
    else:
        print(' '*x+'*'+' '*(i*2-3)+'*')