#第二題 迴圈 
result = ''

for i in range(9):
    for j in range(9):
        if i == 0 or j == 0 or i == 8 or j == 8:
            result += "＊"
        else:
            result += "。"
    result += '\n'

print(result)