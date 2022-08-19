#TA001 錢
import sys
for line in sys.stdin.read().splitlines():
    x,y,z = list(map(int,line.split( )))
    jj = (y+z-x)//2
    a = z - jj
    b = y - jj
    print(a,b,jj)