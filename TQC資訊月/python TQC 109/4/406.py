#406 不定數迴圈-BMI計算
while 1:
    try:
        m = int(input())/100
        kg = int(input())

        BMI = float(f'{kg/m**2:>.2f}')
        if BMI>=30:
            State = 'fat'
        elif BMI>=25 and BMI<30:
            State = 'over weight'
        elif BMI >=18.5 and BMI<25:
            State = 'normal'
        elif BMI<18.5:
            State = 'under weight'

        print(f'BMI: {BMI:>.2f}')
        print(f'State: {State}')
    except:
        break