#二數有權重的相加
import sys

for line in sys.stdin.read().splitlines():
    a,b = list(map(int,line.split()))
    print(4*a+6*b)