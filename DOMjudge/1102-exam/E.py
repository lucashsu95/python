import sys
for line in sys.stdin.read().splitlines():
    a = list(map(str,line.split()))
    
    print(len(a))