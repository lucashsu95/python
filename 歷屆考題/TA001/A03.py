#TA001 整數商餘
while 1:
    try:
        m,n = list(map(int,input().split()))
        Q = m // n
        R = m % n
        print(Q,R)
    except:
        break