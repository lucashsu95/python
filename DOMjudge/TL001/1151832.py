#TL001 判斷輸入的字串是否「全字母」
data = input()
ary = [chr(i) for i in range(97,123)]
for i in data:
    if i in ary:
        ary.remove(i)
if len(ary) == 0:
    print('True')
else:
    print('False')