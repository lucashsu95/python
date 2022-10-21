n = int(input())
ans = []
Lstr = ''
for i in range(1,n+1):
    Lary = list(str(i))
    if '1' in Lary:
        ans.append(i)
        Lstr += str(i)
print('1的個數',Lstr.count('1'))
for i in range(len(ans)):
    print(f"[{i+1}] {ans[i]}")
#5m