#抱怨值問題
n=int(input())
datas=list(map(int,input().split(' ')))
cnt=0
for i in range(1,n):
    for j in range(0,i):
        if datas[i]<datas[j]:
            cnt+=1
print(cnt)
