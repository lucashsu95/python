#1101 閏年 (EOF 版)
while 1:
    try:
        year = int(input())
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print('a leap year')
        else:
            print('a normal year')
    except:
        break