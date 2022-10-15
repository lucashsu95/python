#806 字元次數計算
def compute(Lstr,char):
    return Lstr.count(char)
Lstr = input()
char = input()
print(f'{char} occurs {compute(Lstr,char)} time(s)')