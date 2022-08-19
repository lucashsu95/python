#第八題 迴圈
result = ''

for i in range(9, 0, -1):
    for j in range(9):
        if j == i+3 or j == i+7 or j == i-1 or j == i-5 or j == i-9:
            result += "＊"
        else:
            result += "。"
    result += '\n'

print(result)