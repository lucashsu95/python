#909 聯絡人資料
Lfile = open('data.dat','w+')
data = []
while 1:
    try:
        data = input()
        print(data,file=Lfile)
    except:
        break
print('The content of "data.dat":')
Lfile.seek(0)
print(Lfile.read())
