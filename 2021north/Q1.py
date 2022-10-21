# 試題一(18分)：連分數轉換
data = list(map(int,input().split(',')))[::-1]
total = f'1/{data[0]}'
for i in range(1,len(data)):
    total1,total2= total.split('/')
    total_new = f"{total2}/{int(total2)*data[i]+int(total1)}"
    total = total_new
    # print(total_new)
ans1,ans2= total.split('/')    
print(ans1)
print(ans2)