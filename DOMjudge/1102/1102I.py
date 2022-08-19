n = int(input())
for line in range(n):
    a = input()
    if len(a) == 5:
        print('3')
        continue
    
    if a[1:3] == 'ne' or a[0:2] == 'on' or (a[0] == 'o' and a[-1] == 'e'):
        print('1')
    else:
        print('2')
