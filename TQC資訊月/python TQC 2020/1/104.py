#104 圓形面積計算
import math
num1 = eval(input())

print(f'Radius = {num1}')
print(f'Perimeter = {num1 * 2 * math.pi:.2f}')
print(f'Area = {num1 * num1 * math.pi:.2f}')