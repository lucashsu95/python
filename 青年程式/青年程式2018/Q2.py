#題目 2：月兔(數列)問題 (15%) 
def fun(Lchild,Lfather,t):
    if t > 0:
        fun(Lfather,Lchild + Lfather,t-1)
    else:
        Lfile = open('out.txt','w')
        print(Lfather,file=Lfile)
n = int(input())
fun(1,0,n)
#3m
