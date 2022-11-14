Lstr = input().split()
line = len(Lstr) // 2
for i in Lstr:
    if Lstr.count(i) == line:
        print(i)
        break
