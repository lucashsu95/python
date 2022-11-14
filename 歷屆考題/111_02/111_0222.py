#重複文字只保留一個
Lstr = list(input())
i = 0
while 1:
    if Lstr.count(Lstr[i]) > 1:
        Lstr.remove(Lstr[i])
    else:
        i += 1
    if i == len(Lstr):
        break
print(''.join(Lstr))