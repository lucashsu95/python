#104C排列組合
def fun(Lstr):
    if len(Lstr) >= Lline:
        Llist.append(Lstr)
    for i in range(len(n[0])):
        if n[0][i] not in Lstr:
            fun(Lstr + n[0][i])
for _ in range(int(input())):
    n = input().split(',')
    Llist = []
    Lstr = ''
    Lline = len(n[0])
    fun(Lstr)
    print(int(Llist[int(n[1])-1]) + int(Llist[int(n[2])-1]))