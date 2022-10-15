#901 成績資料
while 1:
    try:
        name,s = input().split()
        Lfile = open('write.txt','a')
        print(name,s,file=Lfile)
    except:
        print('err')
        break