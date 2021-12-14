"""HCF of two numbers"""
n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
while(n2):
    n1,n2=n2,n1%n2 
print(n1)
