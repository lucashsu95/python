#火車堆疊 遞迴

n = int(input())

def fun(n):
    if n == 0 or n == 1:
        return 1

    return fun(n-1) * (4*n-2) / (n+1)

print(int(fun(n)))