#303 迴圈數值相乘
data = int(input())
for i in range(1,data+1):
    for j in range(1,i+1):
        print(f'{i * j:>4d}',end='')
    print()