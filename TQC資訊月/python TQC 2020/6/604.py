#604 眾數
ary = []
while 1:
    try:
        ary.append(int(input()))
    except:
        break
Lnum = Lcount = 0

for i in ary:
    if ary.count(i) > Lcount:
        Lcount = ary.count(i)
        Lnum = i
print(Lnum)
print(Lcount)