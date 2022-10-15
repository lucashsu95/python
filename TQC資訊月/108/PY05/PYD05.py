num = int(input())
Lary = []
def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        if str(num) != str(num)[::-1]:
            return False
    return True
for i in range(2,num):
    if prime(i):
        Lary.append(i)
Lcount = Lcount2 = 1
for i in range(1,len(Lary)+1):
    print(f'{Lary[i-1]:<4d}',end='')
    if Lcount == i or i == len(Lary):
        Lcount2 += 1
        Lcount += Lcount2
        print()
print(sum(Lary))