for _ in range(int(input())):

    data = int(input())
    if data % 2 == 0:
        print(0)
        continue
    data = data // 2
    ary = [1]

    n = 1
    for i in range(1,data+1):
        ary.append(ary[-1]*3-n)
        if i % 2 == 0:
            n += 1
    print(ary[-1]) 
