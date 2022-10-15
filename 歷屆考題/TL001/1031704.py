#TL001 相同數量的母音
import sys
for data in sys.stdin.read().splitlines():
    line = len(data)//2
    data1 = data[0:line].lower()
    data2 = data[line:].lower()
    count = count2 = 0
    for i, j in zip(data1, data2):
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
        if j in ['a', 'e', 'i', 'o', 'u']:
            count2 += 1

    if count == count2:
        print('True')
    else:
        print('False')
