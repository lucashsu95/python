#402 不定數迴圈-最小值
data = 0
Lmax = 0
while data == 9999:
    if Lmax < data:
        Lmax = data
    data = int(input())
print(Lmax)