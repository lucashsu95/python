#第五題 迴圈
result = ''

for i in range(9):
    for j in range(9):
        if i < 5 and j < 5:
            result += "＊"
        else:
            result += "。"
    result += '\n'

print(result)