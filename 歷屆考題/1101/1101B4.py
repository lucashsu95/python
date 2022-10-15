#1101 閏年 (0 尾版)
year = int(input())
while year != 0:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('a leap year')
    else:
        print('a normal year')
    year = int(input())