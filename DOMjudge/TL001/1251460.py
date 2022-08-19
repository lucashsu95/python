#TL001 兩字串的本質比較
st1 = list(input())
st2 = list(input())
st1.sort()
st2.sort()
if st1 == st2:
    print("True")
else:
    print("False")

