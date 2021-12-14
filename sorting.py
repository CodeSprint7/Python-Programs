
"""sorting list based on values
from another list"""
x=[7,3,1,4,2,5,9]
y=['a','b','c','d','e','f','g']
"""sorting y based on the values
of x"""
l=[i for _,i in sorted(zip(x,y))]
print("l=",l)
#after sorting x
x.sort()
print("x=",x)
"""the 1st value is 1 and the
index of 1 before sorting is 2
y[2]=c is the 1st element in l"""