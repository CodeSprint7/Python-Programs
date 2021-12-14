"""Different ways to take input"""
#string input
s=input("Enter a string: ")
#integer input
n=int(input("Enter a number: "))
#multiple inputs in a single line
a,b=map(int,input("Enter a & b: ").split())
#list input
l=list(map(int,input("enter l: ").split()))
#line by line input using lst comprehension
print("enter four numbers")
z=[int(input()) for i in range(4)]
