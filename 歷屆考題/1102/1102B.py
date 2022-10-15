#閏年 (多列版)
n = int(input())
for i in range(n):
    year = int(input())
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        print("a normal year")
    else:
        print("a leap year")