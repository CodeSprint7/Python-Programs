#Diff ways to take input as a list
print("enter nums spereated by space")
l1=list(map(int,input().split()))
print("enter 2 nums line by line")
l2=[]
for i in range(2):
    l2.append(int(input()))
print("enter 2 nums line by line")
#list comprehension
l3=[int(input()) for i in range(2)]
print("enter a string")
s=input()
l4=s.split()
print(l1,l2,l3,l4,sep='\n')