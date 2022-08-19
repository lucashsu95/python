#TL001 持續刪除相鄰相同者
data = list(input())
i = 1
while True:
    if i >= len(data):
        break
    if data[i-1] == data[i]:
        data.remove(data[i-1])
        data.remove(data[i-1])
        i = 0
    else:
        i += 1
data = ''.join(data)
print(data)