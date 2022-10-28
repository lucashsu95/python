def tree(Lfather,Lans):
    Lans.append(Lfather)
    for i in range(len(Lary)):
        if Lfather == Lary[i][1]:
            tree(Lary[i][0],Lans)
    if len(Lans) == n:
        print(', 
        exit()




n = int(input())
Lfather = input()
Lary = []
for i in range(n-1):
    Lary.append(input().split(', '))
#print(Lary)
tree(Lfather,[])
