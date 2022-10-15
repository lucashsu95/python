#701 串列數組轉換
data = int(input())
ary = []
while data != -9999:
    ary.append(data)
    data = int(input())
Ltuple = tuple(ary)
print(Ltuple)
print(f'Length: {len(Ltuple)}')
print(f'Max :{max(Ltuple)}')
print(f'Min :{min(Ltuple)}')
print(f'Sum :{sum(Ltuple)}')