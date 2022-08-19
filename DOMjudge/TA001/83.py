#TA001 質因數
def is_prime(num):
    a_bool = True
    for i in range(2,num//2+1):
        if num % i == 0 :
            a_bool = False
            break
    return a_bool

n = int(input())
ary = []
for i in range(2,n):
    if n % i == 0:
        if is_prime(i):
            ary.append(i)
print(ary)