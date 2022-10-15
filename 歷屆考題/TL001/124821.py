#TL001 字串中的每個位置到指定文字的距離
str1 = list(input())
str2 = input()
ans = []
for i in range(len(str1)):
    ary = []
    for j in range(len(str1)):
        if str1[j] == str2:
            ary.append(abs(j-i))
    ans.append(min(ary))

print(ans)

