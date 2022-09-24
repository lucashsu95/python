#110 正n邊形面蹟計算
import math
Ln = int(input())
Ls = int(input())
print(f'Area = {(Ln*Ls**2)/(4 * math.tan(math.pi / Ln)):.4f}')