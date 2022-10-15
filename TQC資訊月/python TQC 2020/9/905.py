#905 字串資料刪除
fileName = input()
deleteName = input()

Lfile = open(fileName,'r+')
data = Lfile.read()
print('=== Before the deletion')
print(data)
print('=== After the deletion')
data = data.replace(deleteName,'')
print(data)
Lfile.seek(0)
Lfile.write(data)
