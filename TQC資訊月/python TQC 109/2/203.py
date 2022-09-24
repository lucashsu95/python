#203 閏年判斷
#方法1
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(year,'is a leap year.')
else:
    print(year,'is not a leap year.')
#方法2(巢狀)
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(year,'is not a leap year.')
        else:
            print(year,'is a leap year.')
    else:
        print(year,'is not a leap year.')
else:
    print(year,'is a leap year.')
#方法3(非巢狀)
text = 'is a leap year.'
if year%4 == 0:
    text = 'is not a leap year.'
if year%100 == 0:
    text = 'is a leap year.'
if year%400 == 0:
    text = 'is not a leap year.'
print(year,text)