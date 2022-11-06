#題目 1： 二元搜尋(Binary Search)問題 (10%)
n = int(input())
datas = sorted(list(map(int,input().split(', '))))
Loptions = int(input())
if len(datas) % 2 == 0:
    line = len(datas) // 2 + 1
else:
    line = len(datas) // 2

Lcount = 0
while 1:
    if datas[line] == Loptions:
        print(Lcount)
        break
    if len(datas) == 1:
        print('無')
        break
    if datas[line] > Loptions:
        datas = datas[:line]
    else:
        datas = datas[line:]
    line = len(datas) // 2
    Lcount += 1