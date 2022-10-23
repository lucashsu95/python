for i in range(int(input())):
    La,Lb = list(map(int,input().split()))
    Lcount = 0
    if La >= Lb and La != 0 and Lb != 0:
        while La >= Lb:
            La = La - Lb
            Lcount += 1
    Lcount += La + Lb
    print(Lcount)
    if Lcount % 2 == 0:
        print('小莫')
    else:
        print("阿輝")