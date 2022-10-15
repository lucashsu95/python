n = int(input())
a = list(map(int,input().split(' ')))
ary = [2,3,5]
for i in a:
    j = 0
    while True:
        if i % ary[j] == 0:
            print(ary[j])

            i = i // ary[j]
        else:
            j += 1
            if j >= 3:
                break
    if i == 1:
        print("True")
        
    else:
        print("False")          

