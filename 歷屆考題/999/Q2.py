#999Q2Max找最大
import sys
for line in sys.stdin.read().splitlines():
    a = list(map(int,line.split(" ")))
    print(max(a))