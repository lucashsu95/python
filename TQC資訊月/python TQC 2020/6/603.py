#603 數字排序
data = []
while 1:
    try:
        data.append(int(input()))
    except:
        break
data.sort(reverse=True)
print(data[0],data[1],data[2])