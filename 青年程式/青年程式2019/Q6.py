from ast import operator
from re import L


datas = list(map(int,input().split()))
Lary = []
Lary2 = []
def zero(Lary):
    for i in range(len(Lary)-1,-1,-1):
        Lary2.append(Lary[i])
    return Lary2

# def one(Lary):
#     for i in range()

for i in range(datas[0]):
    data = list(map(int,input().split()))
    Lary.append(data)

Lary2 = datas[1] * [[]]
j = 0
for i in range(len(Lary)):
    print(Lary)
    print(Lary[i][len(Lary[0])-1])
    # Lary2[j].append(Lary[i][len(Lary[0])-1])
    # print(Lary2)
    # j += 1
    # if len(Lary2) == j:
    #     break

# Loperator = list(map(int,input().split()))
# for i in Loperator:
#     if i == 0:
#         zero(Lary)
#     elif i == 1:
#         one(Lary)
print(Lary)
print(Lary2)
#31m