#B3 閏年 (Case 多⾏版)
n = int(input())
for i in range(n):
    year = int(input())
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'Case {i+1}: a leap year')
    else:
        print(f'Case {i+1}: a normal year')