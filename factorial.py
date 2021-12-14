#Factorial of a number
num=int(input("Enter a number: "))
if(num>0):
    fact=num 
    for i in range(2,num):
        fact*=i 
    print(num,"factorial is",fact)
else:
    print("NA")