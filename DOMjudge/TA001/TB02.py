#TA001 排序 (Sort) 練習
while 1:
    try:
        data = list(map(int,input().split(',')))
        data.sort(reverse=True)
        print(data)

    except:
        break