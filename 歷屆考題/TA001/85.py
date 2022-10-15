#TA001 所有個數平方和
n = list(map(int,input()))
Lsum = 0
for i in n:
    Lsum += i ** 2
print(Lsum)