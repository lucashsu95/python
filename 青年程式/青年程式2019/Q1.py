datas = list(map(int,input()))
La = Lb = 0
for i in range(len(datas)):
    if i % 2 == 0 :
        La += datas[i]
    else:
        Lb += datas[i]
print(abs(La-Lb))