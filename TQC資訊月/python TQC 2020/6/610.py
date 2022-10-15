#610 平均溫度
data = []
flag = 0
for i in range(12):data.append(eval(input()))
for i in range(0,12,3):
    flag += 1
    print(f'Week {flag}')
    print(f'Day 1:{data[i]}')
    print(f'Day 2:{data[i+1]}')
    print(f'Day 3:{data[i+2]}')