#107A計算字數
n = int(input())
for i in range(n):
    data = input().split(' ')
    Lcount = 0
    for d in data:
        if "s" in d.lower():
            Lcount += 1
    if Lcount>=1:
        print(f'{len(data)},{Lcount}')
    else:
        print(f'{len(data)},0')