#二、迴圈偶數連加
num1 = int(input())
num2 = int(input())
Lcount = 0
for i in range(num1+1,num2+1):
    if i % 2 == 0:
        Lcount += i
print(Lcount)