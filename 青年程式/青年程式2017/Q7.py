#題目 7：搜尋(Search)問題 (15%)
n = int(input())
Lfather_ary = [input()]
Lary = []
Lans = []
for i in range(n-1):
    Lary.append(input().split(', '))

def rec(Lfather_ary):
    global Lans
    Lans.append(Lfather_ary[0])
    for i in range(len(Lary)):
        if Lary[i][1] == Lfather_ary[0]:
            Lfather_ary.append(Lary[i][0])

    Lfather_ary.pop(0)
    if Lfather_ary != []:
        rec(Lfather_ary)

rec(Lfather_ary)
print(', '.join(Lans))
