#猜數字
ans = list(input().split())
for loop in range(int(input())):
    a, b = 0, 0
    x = list(input().split())
    A = [i for i , j in zip(x,ans) if i == j]
    testx = [i for i , j in zip(x,ans) if i != j]
    ansx = [j for i , j in zip(x,ans) if i != j]

    for c in testx:
        if c in ansx:
            b = b+1
            ansx.remove(c)
    print(f"{len(A)}A{b}B")
    print(A)