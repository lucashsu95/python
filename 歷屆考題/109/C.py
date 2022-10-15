#109C時間計算
Ln = int(input())
for i in range(Ln):
    nd, nm, ny = list(map(int, input().split('/')))
    d, m, y = list(map(int, input().split('/')))
    Lage = ny - y
    if nm < m:
        Lage -= 1
    elif nm == m:
        if nd < d:
            Lage -= 1
    print(Lage)
