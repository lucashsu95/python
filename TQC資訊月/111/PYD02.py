num = list(map(int,input().split()))
num.sort()
Lresult = num[0] ** 2 + num[1] ** 2
if Lresult == num[2] ** 2:
    print('直角')
elif Lresult < num[2] ** 2:
    print('鈍角')
elif Lresult > num[2] ** 2:
    print('銳角')
