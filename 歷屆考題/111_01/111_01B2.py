for i in range(int(input())):
    datas = list(map(int,input().split()))
    datas.sort()
    if datas[0] == datas[1] == datas[2] == datas[3]:
        print('square')
    elif datas[0] == datas[1] and datas[2] == datas[3]:
        print('rectangle')
    elif datas[0] + datas[1] + datas[2] >= datas[3]:
        print('quadrangle')
    else:
        print('banana')