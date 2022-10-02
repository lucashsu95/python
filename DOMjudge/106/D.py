#106D幾A幾B
def fun(Lstr):
    if len(Lstr) >= Lline:
        Llist.append(Lstr)
    for i in range(len(n[0])):
        if n[0][i] not in Lstr:
            fun(Lstr + n[0][i])

for _ in range(int(input())):
    n = input().split(',')
    # __排列組合__
    Llist = []
    Lstr = ''
    Lline = len(n[0])
    fun(Lstr)

    # __幾A幾B__
    Lans = Llist[int(n[1])-1]
    Linput = Llist[int(n[2])-1]
    A = B = 0
    Lansx,Ltext = [],[]
    for i,j in zip(Lans,Linput):
        if i == j:
            A += 1
        else:
            Lansx.append(i)
            Ltext.append(j)
    for k in Ltext:
        if k in Lansx:
            B += 1
            Lansx.remove(k)
    print(f'{A}A{B}B')