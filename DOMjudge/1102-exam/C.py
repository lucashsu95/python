import sys
for line in sys.stdin.read().splitlines():
    n = []
    left = 0
    for i in range(len(line)):
        n.append(line[i])
    for j in range(len(n)):
        if n[0] == "+":
            left += int(n[2])+1,int(n[2])+1
            break
        if n[0] == "-":
            left += int(n[2])-1,int(n[2])-1
            break
        if n[2] == "+":
            left += int(n[0]),int(n[0])+1
            break
        if n[2] == "-":
            left += int(n[0]),int(n[0])-1
            break