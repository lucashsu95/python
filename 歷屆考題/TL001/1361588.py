#TL001 加總奇數個數內容的總和
data = list(map(int,input().split()))
Lsum = 0
for i in range(1,len(data)+1):
    if i % 2 != 0:
        for j in range(len(data)):
            if len(data[j:j+i]) < i:
                continue
            Lsum += sum(data[j:j+i])
print(Lsum)