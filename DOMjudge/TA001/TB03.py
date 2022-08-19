#TA001 排序練習 氣泡排序法
while True:
    try:
        data = list(map(int,input().split(', ')))
        for i in range(1,len(data)):
            data2 = data[i-1:i+2]
            data2.sort()
            del data[i-1:i+2]
            Lint = -1
            for j in data2:
                data.insert(i+Lint,j)
                Lint += 1
        print(data)
    except:
        break
