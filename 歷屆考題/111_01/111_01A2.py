Lstart = int(input())
Lend = int(input())
if Lstart > Lend:
    Lstart,Lend = Lend,Lstart
for i in range(Lstart+1,Lend):
    if i % 5 == 2 or i % 5 == 3:
        print(i)