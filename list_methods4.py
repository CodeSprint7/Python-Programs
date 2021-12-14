#List methods part-4 
l1,l2=[1,2,3],[4,5,6]
#merging two lists
l3=l1+l2 
print(l3)
#creating a copy of the list
l4=l1.copy()
print(l4)
#assiging list to new var
l4=l1 
print(l4)
"""adding list to end of the
current list"""
l1.extend(l2)
print(l1)