import sys
sys.stdin.reconfigure(encoding='utf-8')

Lstart = input("起站:")
Lend = input("終站:")
Lback = input("是否單程票")
La = int(input("一般票:"))
Lb = int(input("兒童票:"))
Lc = int(input("軍公教票:"))
Ld = int(input("學生票:"))
Le = int(input("敬老票:"))

Lmap_ary = ['台北','板橋','台中','台南','高雄']
Lmoney_ary = {'台北':['',40,700,1350,1490],'板橋':[40,'',670,1320,1460],'台中':[700,670,'',650,790],'台南':[1350,1320,650,'',140],'高雄':[1490,1460,790,140,'']}
line =Lmap_ary.index(Lend) - Lmap_ary.index(Lstart)
Lmoney_ary[Lstart]
# print(Lmoney_ary)
print(Lstart,line)
result_money = Lmoney_ary[Lstart][line]

Lsum_money = La * result_money + Lb * 0.5 * result_money + Lc * 0.5 * result_money + Ld * 0.7 * result_money + Le * 0.4 * result_money
if Lback == '是':
    Lsum_money *= 2
# print(result_money)
print(int(Lsum_money))
