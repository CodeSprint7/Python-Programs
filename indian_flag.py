from time import sleep,time
import sys
from colorama import Fore as f
n=int(input())
s=f.YELLOW+'\033[1m'+' '*(n+(n//2))+'HAPPY REPUBLIC DAY'
for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(0.10)
print()
for i in range(13):
    if(i==4):
        print(f.RED+'*'*(n+(n//2+2))+f.WHITE+'*'*((n//2)*2-1)+f.RED+"*"*(n+(n//2+1)))
    elif(i==8):
        print(f.GREEN+'*'*(n+(n//2+2))+f.WHITE+'*'*((n//2)*2-1)+f.GREEN+"*"*(n+(n//2+1)))
    elif(i%4==0 and i<=4):
        print(f.RED+'*'*n*4)
    elif(i%4==0 and i>3):
        print(f.GREEN+'*'*n*4)
    elif(i==5 or i==7):
        print(f.WHITE+'*'+' '*(n+(n//2))+'*'*n+' '*(n+(n//2-1))+'*')
    elif(i==6):
        print(f.WHITE+'*'+' '*(n+(n//2-1))+'*'*(n+2)+' '*(n+(n//2-2))+'*')
    else:
        print('*'+' '*(n*4-2)+'*')
    sleep(0.5)

