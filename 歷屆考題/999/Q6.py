#999Q6找相加可能
import sys
for line in sys.stdin.read().splitlines():
    ans1 = ans2 = ''
    a,b = line.split(' ')
    a = list(map(int,a.split(',')))
    b = int(b)
    Lbool = False
    for i in range(len(a)):
        if Lbool:
            break
        for j in range(len(a)):
            if a[i] + a[j] == b:
                ans1 = a.index(a[i])
                ans2 = a.index(a[j])
                Lbool = True
                break
    if Lbool and ans1 != ans2:
        print(ans1,ans2)
    else:
        print("F")
