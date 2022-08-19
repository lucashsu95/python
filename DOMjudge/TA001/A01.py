#TA001 華氏轉攝氏
while 1:
    try:    
        data = int(input())
        data = (data - 32) * 5 / 9
        
        print(f'C={int(data)}')
    except:
        break