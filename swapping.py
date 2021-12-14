#Swapping of two numbers
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
print('before swapping a={},b={}'.format(a,b))
temp=a 
a=b 
b=temp 
print('after swapping a={},b={}'.format(a,b))