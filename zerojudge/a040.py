# a040阿姆斯壯數
while 1:
    try:
        n,m = list(map(int,input().split()))
        ans = []
        for num in range(n,m):
            num2 = num
            num = list(str(num))
            Lsum = 0
            for i in num:
                Lsum += int(i) ** len(num)
            if Lsum == num2:
                ans.append(str(Lsum))
        ans = ' '.join(ans)

        if len(ans) != 0:
            print(ans)
        else:
            print('none')
    except:
        break