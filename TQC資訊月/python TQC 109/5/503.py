#503 連加計算
def compute(num,num2):
    Lcount = 0
    for i in range(num,num2+1):
        Lcount += i
    return Lcount
while 1:
    try:
        num = int(input())
        num2 = int(input())
        print(compute(num,num2))
    except:
        break
