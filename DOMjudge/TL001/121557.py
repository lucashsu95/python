#TL001 反轉句子中的單字
Lstr = input().split()
result = ''
for i in Lstr:
    result += i[::-1] + ' '
print(result)

