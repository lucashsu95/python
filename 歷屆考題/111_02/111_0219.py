Lstr = input()
Lsum = [0,0,0]
for i in range(len(Lstr)):
    if Lstr[i] == 'C' and i + 2 <= len(Lstr)-1:
        if Lstr[i+1] == '+' and Lstr[i+2] == '+':
            Lsum[1] += 1
            continue
    if Lstr[i] == 'C' and i + 1 <= len(Lstr)-1:
        if Lstr[i+1] == '#':
            Lsum[2] += 1
            continue
    if Lstr[i] == 'C':
        Lsum[0] += 1

print(','.join(map(str,Lsum)))
