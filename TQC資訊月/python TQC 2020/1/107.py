#107 數值計算
Lary = []
for i in range(5):
    Lary.append(eval(input()))
print(' '.join(list(map(str,Lary))))
print(f'Sum = {sum(Lary):.1f}')
print(f'Average = {sum(Lary) / len(Lary):.1f}')