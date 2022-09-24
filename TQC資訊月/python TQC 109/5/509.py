#509 最簡分數
import math
def compute(p, q):
    if q == 0:
        return p
    else:
        return compute(q,p % q)
x, y = eval(input())
m, n = eval(input())
p = int((x * n + m * y) / compute(x * n + m * y, y * n))
q = int((y * n) / compute(x * n + m * y, y * n))
print(f'{x}/{y} + {m}/{n} = {p}/{q}')