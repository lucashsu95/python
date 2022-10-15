#906 字串資料取代
LfileName = input()
st1 = input()
st2 = input()
Lfile = open(LfileName,'r+')
data = Lfile.read()

print('=== Before the replacement')
print(data)
print('=== After the replacement')
Lfile2 = data.replace(st1,st2)
print(Lfile2)

Lfile.seek(0)
print(Lfile2,file=Lfile)