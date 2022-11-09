#最大子數列問題
for _ in range(int(input())):
    data = list(map(int,input().split()))
    for i in range(1,len(data)):
        value = data[i]
        data[i] = max(value,value + data[i-1])
    print(max(data))