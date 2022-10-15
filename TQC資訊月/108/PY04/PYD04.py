num = []

while True:
    inp = int(input())
    if inp == -9999:
        break
    num.append(inp)

n = len(num)
Lary = []
# max_slice = max((num[i:j] for i in range(n) for j in range(i+1, n+1)), key=sum)
for i in range(n):
    for j in range(i+1,n+1):
        Lary.append(sum(num[i:j]))
print(max(Lary))
