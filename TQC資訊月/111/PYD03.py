Lmoney,Lapr,Lyear = input().split()
Lcount_year = Lsum = 0
Lapr = eval(Lapr) / 100
# print(Lapr)
for i in range(int(Lyear)):
    Lsum += (int(Lmoney) - Lcount_year) * Lapr / 12
    Lcount_year += int(Lmoney) / int(Lyear)

print(int(Lsum))