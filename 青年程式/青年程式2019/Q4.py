#題目 4：數列問題 (10%)
def fun(Lchild,Lfather,t):
    if t <= n:
        t+=1
        fun(Lfather,Lchild+Lfather,t)
    else:
        print(Lfather+Lchild)

n = int(input())
Lchild = 1
Lfather = 0

fun(Lchild,Lfather,2)
#8m