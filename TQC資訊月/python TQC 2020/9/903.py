#903 成績資料
for i in range(5):
    data = input()
    Lfile = open('write.txt','a')
    print(data,file=Lfile)
Lfile = open('write.txt','r')
Lfile = Lfile.read()
print('Append completed!')
print('Content of "data.txt":')
print(Lfile)