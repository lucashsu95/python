n = int(input())
Lary = [0]
for i in range(n):
    Lary.append(int(input()))
Lary.sort()
Q1 = n * 0.25
Q2 = n * 0.5
Q3 = n * 0.75
if Q1 != int(Q1):
    Q1 = int(Q1) + 1
else:
    Q1 = int(Q1)
if Q2 != int(Q2):
    Q2 = int(Q2) + 1
else:
    Q2 = int(Q2)
if Q3 != int(Q3):
    Q3 = int(Q3) + 1
else:
    Q3 = int(Q3)

print(str(Lary[Q1]) + ',' + str(Lary[Q2]) + ',' + str(Lary[Q3]))
