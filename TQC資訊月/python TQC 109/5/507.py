#507 質數
def compute(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
while 1:
    try:
        num = int(input())
        if (compute(num)):
            print("Prime")
        else:
            print('No Prime')
    except:

        break