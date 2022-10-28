def prime(Lnum):
    for i in range(2,Lnum//2+1):
        if Lnum % i == 0:
            return False
    return True

def rec(Lnow,Lsum,Lstr):
    for i in range(Lnow,n):
        if prime(i):
            if Lsum < n:
                rec(i,Lsum * i,Lstr + '*' + str(i))
            elif Lsum == n:
                print(Lsum,Lstr)
                exit()

n = int(input())
Lsum = 1
rec(2,Lsum,str(2))
