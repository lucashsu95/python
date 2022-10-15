#103B買郵票
n = int(input())
for i in range(n):
    a,b,c,d = list(map(int,input().split(',')))
    for i in range(a+1):
        for j in range(a+1):
            if b*i + c*j == d and j+i == a:
                print(f'{i},{j}')