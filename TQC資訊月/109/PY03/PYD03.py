num = int(input())
ans = 0
for i in range(2,num+1):
    ans += 1 / ((i-1)**0.5 + (i)**0.5)
print(f'{ans:.4f}')