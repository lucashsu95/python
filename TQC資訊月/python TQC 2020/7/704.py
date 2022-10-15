#704 集合條件判斷
Lset = set()
data = int(input())
while data != -9999:
    Lset.add(data)
    data = int(input())
print(f'Lengrth: {len(Lset)}')
print(f'Max: {max(Lset)}')
print(f'Min: {min(Lset)}')
print(f'Sum: {sum(Lset)}')