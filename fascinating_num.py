"""Checkout the description to 
know about the fascinating num"""
n=int(input("Enter a number: "))
x=str(n)+str(n*2)+str(n*3)
count=0 
for i in range(1,10):
    if(x.count(str(i))==1):
        count+=1 
if(count==9):
    print("Is a fascinating num")
else:
    print("Not a fascinating num")