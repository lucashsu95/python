#110T找出比某數小的最大質數10911
def is_prime(num):
    a = True
    for i in range(2,num):
        if num % i == 0:
            a = False
            break
    return a

n = int(input())
for _ in range(n):
    num = int(input())
    for i in range(num-1,1,-1):
        if is_prime(i):
            print(i)
            break
        