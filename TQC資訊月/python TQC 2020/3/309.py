#309 存款總額
Lmoney = int(input())
year = float(input())
month = int(input())
print('{}{:>10s}'.format('Month','Amount'))
for i in range(month):
    print(Lmoney + Lmoney * year / 1200)
    Lmoney = Lmoney + Lmoney * year / 1200
    print(round(Lmoney + Lmoney * year / 1200,2))    
    # print(f'{i+1}{Lmoney}')