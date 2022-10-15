#IMD2021 prob-輸入輸出
while 1:
    try:
        n = int(input())
        if n == 0:
            break
        ary = []
        for i in range(n):
            data = input()
            ary.append(data)
        data = ' '.join(ary)
        print(n)
        print(data)
    except:
        break