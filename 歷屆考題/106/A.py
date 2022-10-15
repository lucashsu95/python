#106A字串問題
n = int(input())
for i in range(n):
    cut = 0
    data = input().split(' ')
    for j in data:
        if 's' in j.lower():
            cut += 1
    if cut != 0:
        print(cut)
    else:
        print('0')