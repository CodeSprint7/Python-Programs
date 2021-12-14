"""String methods part-5"""
"""join all the elements in the list"""
s=['code','sprint']
print(''.join(s))
"""split the string into list at
specified seperator"""
y='welcome to codesprint'
print(y.split(' '))
"""split the string into list from
right side according to the first 
parameter and 1 represents the list 
contains n+1 i.e,1+1=2 elements"""
x='please subscribe to codesprint'
print(x.rsplit(' ',1))