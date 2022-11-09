for _ in range(int(input())):
    datas = list(map(int,input().split()))
    total = datas[0] * datas[1] * datas[2]
    # print(total)
    for i in range(min(datas),1,-1):
        if datas[0] % i == 0 and datas[1] % i == 0 and datas[2] % i == 0:
            print(total // (i**3))
            break 