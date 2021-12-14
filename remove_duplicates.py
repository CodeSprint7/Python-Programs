#Remove duplicates from the list
l=[1,1,1,2,2,3,4,4,5,5]
res=[]
for i in l:
    if(i not in res):
        res.append(i)
print("res=",res)
#2nd way
print("l=",list(set(l)))
#3rd way
for i in l:
    for j in range(l.count(i)-1):
        l.remove(i)
print("l=",l)