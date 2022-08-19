#第十題 迴圈
result = ''

for i in range(9):
    for j in range(9):
        if i-1 >= j:
            result += "。"
        else:
            result += "＊"
    result += '\n'

print(result)