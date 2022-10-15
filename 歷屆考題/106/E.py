#106E網段ID
n = int(input())
for _ in range(n):
    arya, aryb = list(input().split('/'))
    arya = list(map(int, arya.split('.')))
    aryb = list(map(int, aryb.split('.')))
    
    for i in range(len(aryb)):
        aryb[i] = abs(255 - aryb[i])
    ans = []
    
    for k, v in zip(arya, aryb):
        ans.append(str(k | v))

    print('.'.join(ans))
