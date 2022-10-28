Loptions = list(input())
for i in range(len(Loptions)):
    if i % 2 != 0:
        for count in range(int(Loptions[i])):
            print(Loptions[i-1],end='')
