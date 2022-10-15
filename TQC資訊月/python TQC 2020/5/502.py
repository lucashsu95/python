#502 乘積
def compute(x,y):
    ans = x * y
    print(ans)

while 1:
    try:
        num= int(input())
        num2 = int(input())
        compute(num,num2)
    except:
        break