#Alphabet 'M'
n=int(input("enter n: "))
for i in range(n):
    if(i>=n//2):
        print('*'+' '*n+'*')
    else:
        x=(n//2)*2-i*2-1 
        y='*'+' '*i+'*'
        print(y+' '*x+y)