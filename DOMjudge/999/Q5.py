#999Q5因數之和
import sys
for line in sys.stdin.read().splitlines():
    n = int(line)
    factor = 0
    for i in range(1,n+1):
        if n % i == 0:
            factor += i
    print(factor)