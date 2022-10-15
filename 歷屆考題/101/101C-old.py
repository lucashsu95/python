nn = int(input())
for count in range(nn):
    n = int(input())
    left,right = [],[]
    for _ in range(n-1):
        num1,num2 = input().split(',')
        left.append(num1)
        right.append(num2)



    Lcount3 = []
    noright = []
    #noright
    for i in range(len(left)):
        if left[i] not in right:
            noright.append(left[i])

    for title in noright:
        Lcount = title
        Lcount2 = 1
        while Lcount != 0:
            for i in range(len(left)):
                if Lcount == left[i]:
                    # print(Lcount)
                    Lcount2 += 1
                    Lcount = left[i]
            if Lcount == '0':
                break
            Lcount = right[left.index(Lcount)]
        Lcount3.append(Lcount2)

    print(max(Lcount3))
    # print('count:',count)
    if count+1 != nn:
        space = input()
