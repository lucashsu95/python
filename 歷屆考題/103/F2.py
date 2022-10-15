#費氏數列
fibtable = [0, 1]

fibIdx = 2
while fibtable[-1] <= 10000:
    fibtable.append(fibtable[fibIdx-1] + fibtable[fibIdx-2])
    fibIdx += 1
fibtable.pop()
# print('fibtable:', len(fibtable))
# print(fibtable)
n = int(input())
for _ in range(n):
    data = int(input())
    _data = data
    ans = []
    Lindex = len(fibtable) - 1

    while Lindex != 1:
        if data - fibtable[Lindex] >= 0:
            ans.append('1')
            data -= fibtable[Lindex]
        else:
            ans.append('0')
        Lindex -= 1
    firstOneIndex = ans.index('1')

    y = ''.join(ans[firstOneIndex:len(ans)])
    print(str(_data)+'=' + y)

    # fib = fibtable[2:]
    # fib = fib[::-1]
    # z = sum([fib[len(fib)-len(y)+i]
    #         for i in range(len(y)) if y[i] == '1'])
    # print(_data == z)
