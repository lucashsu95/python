#103A數學問題
def is_prime(num):
    for i in range(2,num//2+1):
        if num % i == 0 :
            return False
    return True
n = int(input())
for _ in range(n):
    a,b = list(map(int,input().split(',')))
    ans = 'N'
    if b - a >= 2:
        if is_prime(a) and is_prime(b):
            ans = "Y"
    print(ans)
