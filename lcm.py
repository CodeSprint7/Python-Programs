"""LCM of two numbers"""
n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
m=max(n1,n2)
while(True):
    if((m%n1==0) and (m%n2==0)):
        print(m)
        break 
    m+=1 
