#504 次方計算
def compute(num,num2):
    return num ** num2

while 1:
    try:
        num = int(input())
        num2 = int(input())
        print(compute(num,num2))
    except:
        break
