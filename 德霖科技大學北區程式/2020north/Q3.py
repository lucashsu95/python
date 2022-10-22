datas = input()
left_ary,right_ary = [],[]
Lmax = 0
for i in datas:
    if i in ['+','-','*']:
        right_ary.append(i)
    else:
        left_ary.append(i)
        
right_ary2 = right_ary.copy()
left_ary2 = left_ary.copy()

# print(right_ary,left_ary)
for before in range(len(right_ary)):
    # print(f"{left_ary[before]}{right_ary[before]}{left_ary[before+1]}")
    Lsum = eval(f"{left_ary[before]}{right_ary[before]}{left_ary[before+1]}")
    left_ary[before+1] = Lsum
    if Lsum > Lmax : Lmax = Lsum


# print(right_ary2,left_ary2)
for after in range(len(right_ary2)-1,-1,-1):
    # print(f"{left_ary2[after+1]}{right_ary2[after]}{left_ary2[after]}")
    Lsum = eval(f"{left_ary2[after+1]}{right_ary2[after]}{left_ary2[after]}")
    left_ary2[after] = Lsum
    if Lsum > Lmax : Lmax = Lsum
print(Lmax)