#找索引值
n = int(input())
str = input().split()
for i in range(n):
    a = int(input())
    ans = -1
    for j in range(len(str)):
        if int(str[j]) == a:
            ans = j
            break
    print(ans)
    