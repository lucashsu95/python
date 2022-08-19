#第三題 迴圈
result = ''

for i in range(9):
    for j in range(9):
        if i == 4 or j == 4:
            result += "＊"
        else:
            result += "。"
    result += '\n'

print(result)