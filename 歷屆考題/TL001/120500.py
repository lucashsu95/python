#TL001 鍵盤的一個橫列
Lary = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]
data = input().split()
Lcount = 0
for i in data:
    i = list(i.lower())
    
    for j in range(len(Lary)):
        bool1 = True
        for k in i:
            if k not in Lary[j]:
                bool1 = False
                break
        if bool1:
            Lcount += 1
                
print(Lcount)
        
