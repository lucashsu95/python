#B5 ้ๅนด (EOF ็)
while 1:
    try:
        year = int(input())
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(f'a leap year')
        else:
            print(f'a normal year')
    except:
        break