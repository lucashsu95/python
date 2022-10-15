#605 成積計算
ary = []
while 1:
    try:
        ary.append(int(input()))
    except:
        break
ary.sort()
ary = ary[1:-1]
Lsum = sum(ary)
average = round(Lsum / len(ary),2)
print(Lsum)
print(average)