#702 數組合併排序
ary = []
for i in range(2):
    print(f'Create tuple {i+1}:')
    data = int(input())
    while data != -9999:
        ary.append(data)
        data = int(input())

print(f'Combined tuple before sorting: {tuple(ary)}')
print(f'Combined list after sorting: {sorted(ary)}')