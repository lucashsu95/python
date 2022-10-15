#TL001 找出出現一半次數的數字
data = input().split()
n = len(data)//2
for i in range(len(data)):
    if data.count(data[i]) == n:
        print(data[i])
        break
