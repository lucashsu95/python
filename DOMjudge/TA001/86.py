#TA001 快樂數
CountAry = []
Lsum2 = list(input())
while 1:
    Lsum = 0
    for i in Lsum2:
        Lsum += int(i) * int(i)
    CountAry.append(Lsum)
    Lsum2 = list(str(Lsum))
    if Lsum == 1:
        break
    if CountAry.count(Lsum) >= 2:
        Lsum = 'False'
        break
if Lsum == 1:
    print("True")
else:
    print("False")
