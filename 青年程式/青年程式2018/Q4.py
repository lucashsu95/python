#題目 4：質數(Prime)問題 (10%)
num = int(input())
Lans = []
for i in range(2,num):
    Lbool = False
    for j in range(2,i):
        if i % j == 0:
            Lbool = True
            break
    if Lbool == False:
        Lans.append(i)
print(len(Lans))
#3m
