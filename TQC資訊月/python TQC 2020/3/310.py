import math
num = int(input())
Lsum = 0
for n in range(2, num + 1):
    Lsum += 1 / (math.sqrt(n - 1) + math.sqrt(n))
print(f'{Lsum:.4f}')