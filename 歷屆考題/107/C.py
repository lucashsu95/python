
for i in range(int(input())):
    data = input()
    ary = []
    ans = 'T'
    while data != 1:
        data = list(str(data))
        Lcount = 0
        for i in data:
            Lcount += int(i) ** 2
        if Lcount in ary:
            ans = "F"
            break
        ary.append(Lcount)
        data = Lcount

    print(ans)