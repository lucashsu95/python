#999Q1四數有權重的相加
import sys
for line in sys.stdin.read().splitlines():        
    a,b,c,d = list(map(int,line.split( )))
    print(56*a + 24*b + c*14 + d*6)