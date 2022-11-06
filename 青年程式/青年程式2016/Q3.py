#題目  3：搜尋(Search)問題  (10%)
n = int(input())
Lfather = input()
Lary = []
for i in range(n-1):
    Lary.append(input().split(', '))
Lans = []
def rec(Lfather):
    global Lans
    Lans.append(Lfather)
    for i in range(len(Lary)):
        if Lary[i][1] == Lfather:
            rec(Lary[i][0])


rec(Lfather)
print(', '.join(Lans))
#6m