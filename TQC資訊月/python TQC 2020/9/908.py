#908 單字次數計算
f_name = input()
n = int(input())
Lfile = open(f_name,'r+')
data = Lfile.read().split()
ans = []

for i in data:
    if data.count(i) == n:
        ans.append(i)
ans = list(set(ans))
print(ans)
