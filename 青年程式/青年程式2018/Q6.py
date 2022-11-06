#題目 6：搜尋(Search)問題 (10%)
n = int(input())
Lfather = input()
Lary = []
Lary2 = []
Lans = []
for i in range(n-1):
    Lary.append(list(input().split()))

def rec(Lfather):
    global Lans
    Lans.append(Lfather)
    for i in range(len(Lary)):
        if Lfather == Lary[i][1]:
            rec(Lary[i][0])        


rec(Lfather)
print(' '.join(Lans))