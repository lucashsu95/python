#308 迴圈位數加總
n = int(input())
for i in range(n):
    data = input()
    Lsum = 0
    for i in data:
        Lsum += int(i)
    print(f'Sum of all digits of {data} is {Lsum}')