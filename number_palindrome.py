#Palindrome of a number
n=int(input("Enter a number: "))
temp,res=n,0 
while(n>0):
    res=res*10+(n%10)
    n=n//10 
if(res==temp):
    print("Is a palindrome")
else:
    print("Is not a palindrome")