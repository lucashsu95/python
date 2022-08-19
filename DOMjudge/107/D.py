#107D排列
def fun(Lstr):
    if len(Lstr) == N:
        Llist.append(Lstr)
    for i in range(len(data2)):
        if data2[i] not in Lstr:
            fun(Lstr+data2[i])

for _ in range(int(input())):
    data = input().split(',')
    data2 = data[1:-1]
    Llist = []
    Lstr = ''
    N = int(data[0])
    
    fun(Lstr)
    print(Llist[int(data[-1])-1])  
