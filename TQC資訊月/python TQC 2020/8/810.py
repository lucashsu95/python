#810 最大值與最小值之差
k = int(input())
for i in range(k):
    Lary = list(map(float,input().split()))
    print(f'{max(Lary) - min(Lary):.2f}')