Lmax = []
def tree(Lary,Ldeep,Lnode):
    global Lmax
    for i in range(len(Lary)):
        # print(Lary[i][-1])
        if Lary[i][-1] == Lnode:
            # print('tree:',Lary,Lary[i][0])
            tree(Lary,Ldeep+1,Lary[i][0])
        Lmax.append(Ldeep)

Lary = []
for i in range(int(input())-1):
    Lary.append(input())
tree(Lary,1,'0')
print(max(Lmax))