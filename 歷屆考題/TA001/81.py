#TA001 prob-阿姆斯壯數
n = input()
ans = n
line = len(n)
n = list(n)
Lsum = 0
for i in n:
    Lsum += int(i) ** line
if ans == str(Lsum):
    print("True")
else:
    print("False")
