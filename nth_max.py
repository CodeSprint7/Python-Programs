#nth max element in list
n=int(input("enter nth element:"))
l=[1,2,8,3,10,11,5,16,16]
#removing duplicates
l=list(set(l))
l.sort()
if(len(l)>=n):
    print("nth max=",l[-n])
else:
    print("insufficient length")