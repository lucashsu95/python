#802 字元對應
Lstr = input()
Lsum = []
for i in range(len(Lstr)):
    print(f"ASCII code for '{Lstr[i]}' is {ord(Lstr[i])}")
    Lsum.append(ord(Lstr[i]))
print(sum(Lsum))

