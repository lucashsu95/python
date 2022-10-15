#105C網段ID
n = int(input())
for _ in range(n):
    arya, aryb = list(input().split('/'))
    arya = list(map(int, arya.split('.')))
    aryb = list(map(int, aryb.split('.')))
    ans = []
    
    for k, v in zip(arya, aryb):
        ans.append(str(k & v))

    print('.'.join(ans))
