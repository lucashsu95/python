def prime(Lnum):
    for i in range(2,Lnum//2+1):
        if Lnum % i == 0:
            return False
    return True

n = int(input())
# n = 10000
Lmin = Lmax = 0

for i in range(n-1,1,-1):
    if prime(i):
        Lmin = i
        break
n2 = n + 1
while 1:
    if prime(n2):
       Lmax = n2
       break
    else:
        n2 += 1
# print(Lmax,Lmin)
if Lmax - n > n - Lmin:
    print(n - Lmin)
else:
    print(Lmax-n)

    
    