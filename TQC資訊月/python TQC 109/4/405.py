#406 不定數迴圈-分數等級
data = int(input())
while data != -9999:
    if data>=90:print('A')
    elif data>=80:print('B')
    elif data>=70:print('C')
    elif data>=60:print('D')
    else:print('E')
    data = int(input())
