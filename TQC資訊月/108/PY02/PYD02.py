data = int(input())

ans = 0
for i in range(1,data+1):
    ans += (-1)**(i+1) / (2*i-1)
print(f'{4*ans:.4f}')