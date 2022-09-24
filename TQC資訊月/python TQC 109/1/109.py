#109 正五邊形面積計算
import math
num = int(input())
print(f'Area = {(5*num**2)/(4 * math.tan(math.pi / 5)):.4f}')