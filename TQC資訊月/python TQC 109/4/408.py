#408 奇偶數個數計算
even = 0
odd = 0
while 1:
    try:
        data = int(input())
        if data % 2 == 0:
            even += 1
        else:
            odd += 1
    except:
        print(f'Even numbers: {even}\nOdd numbers: {odd}')
        break

