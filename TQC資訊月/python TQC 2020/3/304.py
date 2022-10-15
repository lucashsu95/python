#304 迴圈倍數總和
num = int(input())
Lsum = 0
for i in range(1,num):
    if i % 5 == 0:
        Lsum += i
print(Lsum)