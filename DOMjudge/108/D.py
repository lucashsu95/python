#108D求餘數
for _ in range(int(input())):
    x,y,m = list(map(int,input().split()))
    Lresult = (x**y) % m
    print(Lresult)