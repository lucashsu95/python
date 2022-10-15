#IMD2020運算子
n = int(input())
for _ in range(n):
    a,b = list(map(int,input().split(' ')))
    if a < b :
        print('<')
    elif a > b:
        print('>')
    elif a == b:
        print('=')
