#404 數字反轉判斷
data = input()
if data[0] == '-':
    data = data[1:]
    data = data[::-1]
    data = '-' + data
else:
    data = data[::-1]
print(data)