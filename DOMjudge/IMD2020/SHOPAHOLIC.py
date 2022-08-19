#IMD2020省錢大作戰
for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    data.sort(reverse=True)
    ans = 0
    while len(data) >= 3:
        value = data[:3]
        ans += min(value) 
        data = data[3:]
    print(ans)