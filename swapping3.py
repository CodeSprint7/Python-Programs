"""Swapping of two numbers without using
third variable"""
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
print('before swapping a={},b={}'.format(a,b))
a=a+b 
b=a-b 
a=a-b 
print('after swapping a={},b={}'.format(a,b))