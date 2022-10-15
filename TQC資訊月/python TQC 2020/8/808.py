#808 社會安全碼
Lstr = input().split('-')
for i in Lstr:
    if not i.isdigit():
        print('Invalid SSN')
        break
else:
    print('Valid SSN')
