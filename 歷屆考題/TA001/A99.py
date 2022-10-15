#TA001 輸出星期幾
mon_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for _ in range(int(input())):
    month,day = list(map(int,input().split()))
    daysum = 0
    if month == 1:
        daysum = day
    else:
        daysum = sum(mon_days[:month-1]) + day
        
    # print(daysum)
    Lcount = 4
    for i in range(daysum):
        Lcount += 1
        if Lcount == 7:
            Lcount = 0
    print(week[Lcount])
    #print(daysum)