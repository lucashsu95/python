#IMD2021 prob-根據ABC的順序輸出數字的順序
n = list(map(int,input().split(' ')))
n.sort()
Lorder = input()

if Lorder == 'ABC':
    print(f'{n[0]} {n[1]} {n[2]}')
elif Lorder == "ACB":
    print(f'{n[0]} {n[2]} {n[1]}')
elif Lorder == "BAC":
    print(f'{n[1]} {n[0]} {n[2]}')
elif Lorder == 'BCA':
    print(f'{n[1]} {n[2]} {n[0]}')
elif Lorder == 'CAB':
    print(f'{n[2]} {n[0]} {n[1]}')
elif Lorder == 'CBA':
    print(f'{n[2]} {n[1]} {n[0]}')