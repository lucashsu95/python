#108C包含某個數字
n = int(input())
for _ in range(n):
    a,b,c = list(map(int,input().split(' ')))
    record = []
    for i in range(a,b+1):
        if str(c) in str(i):
            record.append(str(i))
    print(len(record))
    