#105B摩斯電碼
n = int(input())
Lary = ['-----', '.----', '..---', '...--', '....-',
        '.....', '-....', '--...', '---..', '----.']
for i in range(n):
    ans = ''
    data = input().split(' ')

    for j in data:
        for k in Lary:
            if j == k:
                ans += str(Lary.index(j))
    print(ans)
