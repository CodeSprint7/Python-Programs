#Palindrome of a string
s=input("Enter a string: ")
if(s==s[::-1]):
    print("Is a palindrome")
else:
    print("Is not a palindrome")