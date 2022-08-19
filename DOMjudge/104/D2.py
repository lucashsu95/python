#104最大公約數計算(沒用模組)
for _ in range(int(input())):
    data = list(map(int,input().split(',')))
    for i in range(1,len(data)):
        while data[i-1] % data[i] != 0:
            print(i,data)
            x = data[i]
            data[i] = data[i-1] % data[i]
            data[i-1] = x
    print(data[i])
    #print(data)
    