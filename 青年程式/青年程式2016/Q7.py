#題目  7：解碼(Decoding)問題  (15%) 
Loptions = list(input())
for i in range(len(Loptions)):
    if i % 2 != 0:
        for count in range(int(Loptions[i])):
            print(Loptions[i-1],end='')
