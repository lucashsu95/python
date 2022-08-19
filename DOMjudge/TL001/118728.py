#TL001 指定範圍間的「可自我整除」之數
def fun(Lstr):
    Llist = list(map(int,Lstr))
    Lint = int(Lstr)
    Lbool = True
    for i in Llist:
        if i == 0:
            Lbool = False
            break    
        elif Lint % i != 0:
            Lbool = False
            break
    return Lbool
    
start = int(input())
end = int(input())
ans = []
for i in range(start,end+1):
    if fun(str(i)):
        ans.append(i)
print(ans)