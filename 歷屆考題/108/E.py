#108E出現次數最多的DNA列
for _ in range(int(input())):
    La,Lb = list(map(int,input().split()))
    data,ary,ans = [],[],[]
    ary2 = ['A','C','G','T']
    for i in range(Lb): ary.append([])
    for i in range(La): data.append(input())

    for i in data:
        for j in range(Lb):
            ary[j].append(i[j])
    #ary = [[data[j][i] for j in range(La)] for i in range(Lb)]

    for i in ary:
        ary3 = [0,0,0,0]
        for j in range(len(i)):
            if i[j] in ary2:
                ary3[ary2.index(i[j])] += 1
        if ary3[0] == 4:
            ans.append('A')
        else:
            ans.append(ary2[ary3.index(max(ary3))])
    print(''.join(ans))


