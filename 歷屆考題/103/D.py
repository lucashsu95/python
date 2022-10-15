#103D計算兩個人之間共同朋友的數量
n = int(input())
for i in range(n):
    ID_a = input().split()
    ID_b = input().split()
    ID_a.pop(0)
    ID_b.pop(0)
    if len(ID_a) > len(ID_b):
        ID_a, ID_b = ID_b, ID_a
    Lcount = []
    for i in ID_b:
        if (i in ID_a )and( i not in Lcount):
            Lcount.append(i)
    # Lcount = list(set(Lcount))
    print(len(Lcount))