"""Automorphic number--> if the last
digits of the square of the number
give the same number."""
#n=25 25*25=625 last two digits are 25
n=int(input())
s=n**2 
res=s%pow(10,len(str(n)))
if(res==n):
    print("Automorphic number")
else:
    print("Not a automorphic number")