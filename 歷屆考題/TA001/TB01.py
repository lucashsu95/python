#TA001 四數有權重的相加 之後再算 費波那契數
def fib(n):
    i = count = 0
    j = 1
    
    while count < n:
        i , j = j , i + j
        count += 1
    return i
while 1:
    try:
        a,b,c,d = list(map(int,input().split()))
        result = 56*a+24*b+14*c+6*d
        print(fib(result))
    except:
        break