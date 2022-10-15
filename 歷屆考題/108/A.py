#108A統計答案得分
for _ in range(int(input())):
    a = input()
    Lcut = 0
    answer = 0
    for i in a:
        if i == 'O':
            Lcut += 1
            answer += Lcut
        elif i == 'X':
            Lcut = 0
    print(answer)
        
        

    