#103C在兩字串中,共同出現的英文字母
for i in range(int(input())):
    Lstr = []
    string_a = input()
    string_b = input()

    if len(string_a) > len(string_b):
        string_a, string_b = string_b, string_a
    for i in string_a:
        if i in string_b:
            Lstr.append(i)
    Lstr = list(set(Lstr))
    Lstr.sort()
    if Lstr != []:
        print(''.join(Lstr))
    else:
        print('N')