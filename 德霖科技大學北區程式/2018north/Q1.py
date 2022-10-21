#試題一(14分)：日期資訊查詢
import datetime
arr_year = [0,31,28,31,30,31,30,31,31,30,31,30,31]
arr_weekday = ['','星期一','星期二','星期三','星期四','星期五','星期六','星期日',]
year,month,day = list(map(int,input().split('/')))

#一年的第幾天
now_day = sum(arr_year[:month]) + day

#一年的第幾週
now_week,week_mod = sum(arr_year[:month]) // 7,sum(arr_year[:month]) % 7
week_mod += day
if week_mod % 7 != 0:
    now_week += week_mod // 7 + 1
else:
    now_week += week_mod

#該月份有幾天
now_month = arr_year[month]

#當天是星期幾
now_weekday = arr_weekday[datetime.date(year,month,day).isoweekday()]

print('一年的第幾天:',now_day)
print('一年的第幾週:',now_week)
print('該月份有幾天:',now_month)
print('當天是星期幾:',now_weekday)
