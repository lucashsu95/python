#907 詳細資料顯示
f_name = input()
Lfile = open(f_name,'r+')
Lcount = Lword = Lchar =  0
for i in Lfile:
    Lcount += 1
    Lword_2 = i.split(' ')
    Lword += len(Lword_2)
    Lchar += len(i)

Lchar -= Lword + 1
print(f'{Lcount} line(s)')
print(f'{Lword} word(s)')
print(f'{Lchar} character(s)')

