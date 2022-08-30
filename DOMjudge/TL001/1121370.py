#TL001 以遞升及遞減重組字串
str1 = list(sorted(input()))
ans = ''
while str1 != []:
    str2 = ''
    Lstr = str1.copy()
    for i in Lstr:
        if i not in str2:
            str2+=i
            str1.remove(i)
    str1 = str1[::-1]
    ans += str2

print(ans)