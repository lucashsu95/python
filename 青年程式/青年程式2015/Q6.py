#題目 6：孿生質數問題
def prime(Lnum):
    for i in range(2,Lnum//2+1):
        if Lnum % i == 0:
            return False
    return True

n = int(input())
Lbool = False
for i in range(n):
    Lnum,Lnum2 = list(map(int,input().split(',')))
    # print(Lnum,Lnum2)
    if prime(Lnum):
        if prime(Lnum2):
            if abs(Lnum - Lnum2) == 2:
                Lbool = True
    if Lbool :
        print('是')
    else:
        print('不是')

