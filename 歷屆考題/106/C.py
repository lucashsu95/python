#106C信用卡卡號、幾A幾B
n = int(input())
for _ in range(n):
    sum = 0
    data = input()

    for i in range(len(data)):
        num = int(data[i])

        if i % 2 == 0:
            num *= 2
        
        if num >= 10:
            num -= 9

        sum += num

    if sum % 10 == 0:
        print('T')
    else:
        print('F')