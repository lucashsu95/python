#108 座標距離計算
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

print(f'( {x1} , {y1} )')
print(f'( {x2} , {y2} )')

print(f'Distance = {((x1 - x2)**2 + (y1 - y2)**2)**0.5:.4f}')