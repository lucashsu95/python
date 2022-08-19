#猜數字
ans = list(input().split())
n = int(input())
for _ in range(n):
    a, b = 0, 0
    testx, ansx = [],[]
    x = list(input().split())

    for i in range(4):
        if x[i] == ans[i]:
            a += 1
        else:
            testx.append(x[i])
            ansx.append(ans[i])

    for c in testx:
        if c in ansx:
            b = b+1
            ansx.remove(c)
    print(f"{a}A{b}B")