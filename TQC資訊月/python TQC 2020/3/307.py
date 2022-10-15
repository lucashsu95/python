#307 乘法表
num = int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        print(f'{j:^2d}* {i:^2d}={i * j:^4d}',end='')
    print()