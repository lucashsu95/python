#題目 6：矩陣轉換問題(15%)
datas = list(map(int, input().split()))
Lary = []


def zero(Lary):
    Lary2 = []
    for i in range(len(Lary)-1, -1, -1):
        Lary2.append(Lary[i])
    return Lary2

def one(Lary):
    Lary2 = []
    for i in range(len(Lary[0])):
        Llist = []
        for j in range(len(Lary)):
            Llist.append(Lary[j][i])
        Lary2.append(Llist)
    Lary2.reverse()
    return Lary2


for i in range(datas[0]):
    Lary.append(list(map(int, input().split())))
options = list(map(int, input().split()))

while len(options) > 0:
    print(Lary)
    if options[0] == 0:
        Lary = zero(Lary)
    elif options[0] == 1:
        Lary = one(Lary)
    options.pop(0)
print(len(Lary),len(Lary[0]))
