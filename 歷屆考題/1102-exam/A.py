import sys
for line in sys.stdin.read().splitlines():
    a,b = line.split()
    print(int(a)+int(b))
    