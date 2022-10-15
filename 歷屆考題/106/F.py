#106F大數排序問題
n = int(input())
for _ in range(n):
    data = list(map(int,input().split(',')))
    
    dataSort = sorted(data)
    # print('data:',data)
    # print('dataSort',dataSort)
    ans = []
    
    for i in range(len(data)):
        ans.append(str(dataSort.index(data[i])+1))
        
    Lstr = ', '.join(ans)
    print(Lstr)
    
        
