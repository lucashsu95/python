n = int(input())
Lary = [1, 1, 2, 5]

for i in range(4, n+1):
    Lary.append(int(Lary[i-1] * (4 * i - 2) / (i + 1)))

print(Lary[n])