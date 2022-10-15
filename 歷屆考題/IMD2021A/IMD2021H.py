#IMD2021A 完美數、盈數、虧數
#(超時)
n = input()
data = input().split()
for i in data:
    Llist = []
    for j in range(1,int(i)):
        if int(i) % j == 0:Llist.append(j)
    if sum(Llist) == int(i):print('perfect')
    elif sum(Llist) > int(i):print('abundant')
    elif sum(Llist) < int(i):print('deficient')
#--------------------------------------



# n = input()
# data = list(map(int,input().split()))
# Lmax = max(data)
# Lmin = min(data)
# table = []
# for i in range(Lmin,Lmax+1):
#     Llist = []
#     for j in range(1,i):
#         if i % j == 0:
#             Llist.append(j)
#     table.append(sum(Llist))
# for i in data:
#     ans = table[i - Lmin]
#     if ans > i:
#         print('abundant')
#     elif ans == i:
#         print('perfect')
#     elif ans < i:
#         print('deficient')