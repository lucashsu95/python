#題目 4：N 多邊形問題
val = int(input())

weg = (val * (val - 3)) / 2
print(int(weg)+val)

a = (val - 2) * 180
print(f'{a} 度')
