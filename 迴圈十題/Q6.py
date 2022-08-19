#第六題  迴圈
result = ''

for i in range(9):
    for j in range(9, 0, -1):
        if j-1 == i:
            result += "＊"
        else:
            result += "。"
    result += '\n'

print(result)