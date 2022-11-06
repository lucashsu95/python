#題目 4：求陣列的連續子陣列元素值總和的最大值(12%)
n = int(input())
datas = list(map(int,input().split(',')))
Lmax = [-1,len(datas)+1,0,0,len(datas)+1] #[總計最大值,長度,東西,開始,結束]
for i in range(0,len(datas)-1):
    for j in range(i+2,len(datas)+1):
        #print(i,j)
        Lsum = sum(datas[i:j])
        Lline = len(datas[i:j])
        if (Lsum == Lmax[0] and Lline < Lmax[1]) or (Lsum > Lmax[0]):
            Lmax[0] = Lsum
            Lmax[1] = Lline
            Lmax[2] = datas[i:j]
            Lmax[3] = i
            Lmax[4] = j
print(f'元素值總和的最大值：{Lmax[0]}')
print(f'子陣列的開始位置：{Lmax[3]}')
print(f'子陣列的結束位置：{Lmax[4]}')
# print(Lmax)
