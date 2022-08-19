#TL001 以遞升及遞減重組字串
st1 = list(input())
st2 = ''
ans = []
st1.sort()
while st1 != []:
    ans.append(st2)
    st2 = ''
    st = st1.copy()
    for i in range(len(st)):
        if st[i] not in st2:
            st2 += st[i]
            st1.remove(st[i])
    ans.append(st2)
    st2 = ''
    st = st1.copy()
    for i in range(len(st)-1,0,-1):
        #print('i',i)
        if st[i] not in st2:
            st2 += st[i]
            st1.remove(st[i])
print(''.join(ans))