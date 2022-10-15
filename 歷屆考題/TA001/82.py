#TA001 完美數
n = int(input())
ary = []
Lsum = 0
for i in range(1,n):
    if n % i == 0:
        ary.append(i)
for j in ary:
    Lsum += j
if Lsum == n:
    print("True")
else:
    print("False")
