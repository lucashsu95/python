#第一題  迴圈
result = ''

for i in range(9):
    for j in range(9):
        if i == j:
            result += "＊"
        else:
            result += "。"
    result += '\n'

print(result)