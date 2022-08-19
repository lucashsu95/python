n = int(input())
ary = []
for i in range(n):

    a = input().split()
    ary.append(a)
    sum = 0

ans = input()

for j in range(len(ary)):
    if ary[j][1] == "+=":
        #print(ary[j])
        p = 0
        x = 0
        y = 0
        for k in range(len(ary)):
            if ary[k][1] == "=" and ary[k][0] == ary[j][0]:
                x = int(ary[k][2])
                p=k
            if ary[k][1] == "=" and ary[k][0] == ary[j][2]:
                y = int(ary[k][2])

        ary[p][2] = x+y

for j in range(len(ary)):
    if ary[j][1] == "=" and ary[j][0] == "c":
        print(ary[j][2])

    #for j in range():  

