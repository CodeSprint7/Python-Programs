"""Swapping of two numbers without using
third variable"""
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
print('before swapping a={},b={}'.format(a,b))
a,b=b,a 
print('after swapping a={},b={}'.format(a,b))