#109A找出最大和第二大的數字
for i in range(int(input())):
    #a = input().split()
    a = list(map(int,input().split()))
    ary = []
    for j in a:
        ary.append(j)
    ary.sort(reverse=True)
    print(ary[0],ary[1])
