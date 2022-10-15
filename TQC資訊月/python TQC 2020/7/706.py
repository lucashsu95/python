#706 全字母句
n = int(input())
for i in range(n):
    Lstr = set(input().lower())
    if len(Lstr) >= 26:
        print("True")
    else:
        print("False")