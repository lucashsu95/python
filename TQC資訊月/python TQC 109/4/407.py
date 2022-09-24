#407 不定數迴圈-閏年判斷
year = int(input())
while year != -9999:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year')
    year = int(input())
