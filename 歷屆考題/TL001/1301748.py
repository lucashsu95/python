#TL001 計算不重複數字的總和
ary = [i for i in range(1,10)]
data = list(map(int,input().split()))
for i in ary:
    if data.count(i) >= 2:
        while i in data:
            data.remove(i)
print(sum(data))
