#最大偶數和
n=input()
num = list(map(int,input().split()))
ans=sum(num)
if ans %2 == 0:
    print(ans)
else:
    num.sort()
    for i in num:
        if i % 2 != 0:
            ans -= i
            break
    print(ans)

