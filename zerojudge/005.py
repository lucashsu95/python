# a005EVa的回家作業
for t in range(int(input())):
    n = list(map(int, input().split()))
    print(*n, '', end='')

    if n[1]/n[0] == n[2]/n[1]:
        print(int(n[3]*(n[1]/n[0])))
    else:
        print((n[3])+(n[1]-n[0]))
