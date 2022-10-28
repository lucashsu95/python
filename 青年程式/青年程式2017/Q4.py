#題目 4：費氏數(Fibonacci)問題 (15%) 

def fun(Lchild,Lfather,t):
    if t >0:
        fun(Lfather,Lchild+Lfather,t-1)
    else:
        print(Lfather)
n = int(input())
fun(1,0,n)
