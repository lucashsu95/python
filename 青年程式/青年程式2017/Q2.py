#題目2:質數(Prime)加法分解問題 (15%)
def prime(num):
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True

def fun(num,s,t):
    t1 = 0
    for i in range(num-1,-1,-1):            
        t1 = t + prime_ary[i]
        # print(f"{t1} = {t} + {prime_ary[i]}")
        if t1 < data:
            fun(i,s+'+'+str(prime_ary[i]),t1)
        if t1 == data:
            # print(s+'+'+str(prime_ary[i]))
            ans = s+'+'+str(prime_ary[i])
            ans_Lary.append(ans[1:])
ans_Lary = []
data = int(input())
prime_ary = []
for i in range(2,data):
    if prime(i):
        prime_ary.append(i)
# print(prime_ary)
fun(len(prime_ary),'',0)
print(prime_ary)
print(ans_Lary)
print(ans_Lary[0])
