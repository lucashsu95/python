#306 迴圈階乘計算
num = int(input())
ans = 1
for i in range(1,num+1):
    ans *= i
print(ans)
